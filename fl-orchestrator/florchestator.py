
from asyncio import constants
from crypt import methods
from random import randint
import websockets
import asyncio
from flask import Flask,send_from_directory, request, jsonify, make_response, render_template
import ast
import shutil
import json
import pymongo
import gridfs
import time
import copy
import logging
import requests as req
import constants as const
import threading
import sys

import requests as req

# //DELETE declarado previamente
from constants import *

from utils import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)


app = Flask(__name__)

# Declare firstInstance for controlling the first execution of Orchestrator
firstInstance = True
repositoryModels = ''
available_ui_clients = 0
active_connections = set()
#===========================================================
#================ API USING SWAGGER ========================
#===========================================================

@app.route('/')
def get_root():
    print('sending root')
    return render_template('index.html')

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')

#===========================================================
#================ CHECKING CONNECTION TO MONGODB ===========
#===========================================================
try:
    instance = pymongo.MongoClient(f'mongodb://{const.DB_HOST_NAME}:{const.DB_PORT}/')
    database = instance['assist_iot']
    #Recover list of databases
    dblist = instance.list_database_names()

    if 'assist_iot' in dblist:
        logging.warning('The database exists: assist_iot')
        

    #Check if the collection exists
    collist = database.list_collection_names()
    if 'configuration_models' in collist:
        logging.warning('The collection exists: configuration_models')

    elif 'aditional_data_model' in collist:
        logging.warning('The collection exists: aditional_data_model')

    collection_adm = database['aditional_data_model'] #collection_adm -> Collection Aditional Data Model

    collection = database['configuration_models']
except Exception as ex:
    logging.error("ERROR TO CONNECT MONGO",ex.args)
#===========================================================
#================ API USING MONGODB ========================
#===========================================================

# Recover all models from MongoDB
@app.route('/models',methods = ['GET','POST']) # type: ignore
def models():
    try:
        if(request.method == 'GET'):
            models = collection.find({},{'_id':0})
            #sendNotification('SUCCESS', 'Models retrieved from MongoDB', '')

            return make_response(jsonify({ "data": list(models)}), 200)
        else:
            return make_response(jsonify({ "data" : "This endpoint does not support a POST"}), 200)
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, '')

#===============================================================
#============= CALL OTHER COMPONENTS ===========================
#===============================================================
@app.route('/databases', methods = ['GET']) # type: ignore
def download_models():
    try:
        instance_repository = pymongo.MongoClient(f'mongodb://{const.FL_REPOSITORY_HOSTNAME}/') # type: ignore
        database_repository = instance_repository['repository_grid']
        #Recover list of databases
        dblist_repository = instance_repository.list_database_names()

        data = database_repository.fs.files.find_one({'filename': 'model/classification/base2'})

        my_id = data['_id'] # type: ignore

        #db = client.repository
        db_grid = instance_repository.repository_grid
        fs = gridfs.GridFS(db_grid)

        outputdata = fs.get(my_id).read()

        download_location = "./data/model.pickle"
        output = open('model.pickle', "wb")
        output.write(outputdata)
        output.close()

        return make_response(jsonify({ "data" : "It's OK"}), 200)

    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'download_models method')
        

def getModels_FLRepository():
    try:
        status = False
        query_models = req.get(f'http://{const.FL_REPOSITORY_HOSTNAME}:{const.FL_REPOSITORY_PORT}/model/')
        if (query_models.status_code == 200):
            status = True

            #sendNotification('SUCCESS', 'Models retrieved from Repository', json.dumps(json.loads(query_models.text)))

            response = json.loads(query_models.text)
            
            return response
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'getModels_FLRepository method')

    return False, []

def sendInfoLocalOperation(model, configuration,check):
    global active_connections
    logging.info('Sending configuration to Local Operation')
    result = False
    try:
        if check == True:
            config_copy = configuration.copy()
            eval_metrics_array = []
            if isinstance(configuration['eval_metrics'],str):
                eval_metrics_array.append(configuration['eval_metrics'])
            elif isinstance(configuration['eval_metrics'],list):
                eval_metrics_array = configuration['eval_metrics']

            lo_test ={}
            del config_copy["_id"]
            del config_copy["min_fit_clients"]
            del config_copy["min_available_clients"]
            del config_copy["strategy"]
            del config_copy["model_id"]
            del config_copy["status"]
            del config_copy["checked"]
            del config_copy["meta"]
            del config_copy["adapt_config"]
            del config_copy["min_eval_clients"]
            del config_copy["configuration_id"]
            del config_copy["stopping_flag"]
            del config_copy["stopping_target"]
            for item in config_copy:
                if item == 'number_of_rounds':
                    lo_test["num_rounds"] = config_copy[item]
                lo_test[item] = config_copy[item]
        
            del lo_test["number_of_rounds"]
            lo_test["eval_metrics"] = eval_metrics_array
            lo_test["training_id"] = str(model['training_id'])

            headers = {
                'Content-Type': 'application/json'
            }
            set_copy = active_connections.copy()
            for websocket, host,port, status in set_copy:
                query_status = req.get(f'http://{host}:{port}/job/status', headers=headers)
                if query_status:
                    query_local_operations = req.post(f'http://{host}:{port}/job/config/' + str(model['training_id']), headers=headers, data = json.dumps(lo_test))
            
            if query_local_operations.text == '200': # type: ignore
                result = True
            else:
                result = False
        else:
            message = {"status":"STOP" , "message":"Not enough Local Operations"}
            logging.warning(f'NOT HAPPY PATH SCENARIO TRAINING COLLECTOR: {message}')
            result = False
            sendNotification('STOP',json.dumps(message),'Stop Not Enough LO')
    except Exception as ex:
        logging.error('Error to send configuration to the Local Operations')
        logging.error('ERROR: ',ex.args)
        sendNotification('ERROR', ex.args, '')
        result = False
    
    return result

def sendInfoTrainingCollector(model, configuration,check):
    logging.info('Sending configuration to Training Collector')
    result = False
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        if check == True:
            dataTrainingCollector = {
            "strategy" : configuration['strategy'],
            "model_name" : configuration['model_name'],
            "model_version" : configuration['model_version'],
            "adapt_config" : configuration['adapt_config'],
            "server_conf":{
                "num_rounds" : configuration['number_of_rounds']
            },
            "strategy_conf":{
                "min_fit_clients" : configuration['min_fit_clients'],
                "min_available_clients" : str(configuration['min_available_clients']),
                "min_evaluate_clients" : configuration['min_eval_clients']
            },
            "privacy-mechanisms":configuration['privacy-mechanisms'],
            "client_conf" : configuration['config'],
            "configuration_id" : model['configuration_id'],
            "stopping_flag" : configuration['stopping_flag'],
            "stopping_target" : configuration['stopping_target']
            }
            query_training_collector = req.post(f'http://{const.FL_TRAINING_COLLECTOR_HOSTNAME}:{const.FL_TRAINING_COLLECTOR_PORT}/job/config/' + str(model['training_id']), headers=headers, data = json.dumps(dataTrainingCollector))

            if query_training_collector.text == '200':
                result = True
            else:
                result = False
        else:
                message = {"status":"STOP" , "message":"Not enough Local Operations"}
                logging.warning(f'NOT HAPPY PATH SCENARIO TRAINING COLLECTOR: {message}')
                query_training_collector = req.post(f'http://{const.FL_TRAINING_COLLECTOR_HOSTNAME}:{const.FL_TRAINING_COLLECTOR_PORT}/job/stop', headers=headers, data = json.dumps(message))
                result = False
                sendNotification('STOP',json.dumps(message),'Stop Not Enough LO')
                

    except Exception as ex:
        logging.error('Error to send configuration to the Training Collector')
        logging.error('ERROR: ', ex.args)
        sendNotification('ERROR', ex.args, '')
        result = False
        
    return result

def insertAditionalData():
    collection = database['aditional_data_model']
    data = const.DATA_INSERT
    count = collection.count_documents({})

    if count > 0:
        res = collection.find()
        for item in res:
            delItem = collection.delete_one({'checked':item['checked']})

    result = collection.insert_one(data) # type: ignore

    if result._WriteResult__acknowledged == True: # type: ignore
        return 'True'
    
    return 'False'

def exist(c,m):

    if 'configuration_id' in c:
        print('')
    else:
        c['configuration_id'] = randint(0,50)

    if c['configuration_id'] & m['configuration_id']:
        del c['configuration_id']
        del m['configuration_id']

        if c == m:
            return 'True'
        else:
            return 'False'



#==========================================================
#============= ORCHESTRATOR API ===========================
#==========================================================

#Get model dataa
@app.route('/addModelData',methods = ['GET'])
def insertAditionalModelData():
    result = insertAditionalData()
    return result
@app.route('/modelData',methods = ['GET'])
def recoverMergedModelData():
    try:
        response = getModels_FLRepository()
        collection = database['aditional_data_model']
        aditional_data_model = collection.find({},{'_id':0})
        arr = []
        for item in aditional_data_model:
            for index in range(len(response)):
                response[index]['adapt_config'] = item['adapt_config'] # type: ignore
                response[index]['client_type_id'] = item['client_type_id'] # type: ignore
                response[index]['config'] = item['config'] # type: ignore
                response[index]['eval_func'] = item['eval_func'] # type: ignore
                response[index]['eval_metrics'] = item['eval_metrics'] # type: ignore
                response[index]['eval_metrics_twotronics'] = item['eval_metrics_twotronics'] # type: ignore
                response[index]['min_available_clients'] = item['min_available_clients'] # type: ignore
                response[index]['min_fit_clients'] = item['min_fit_clients'] # type: ignore
                response[index]['num_classes'] = item['num_classes'] # type: ignore
                response[index]['num_rounds'] = item['num_rounds'] # type: ignore
                response[index]['optimizer_config'] = item['optimizer_config'] # type: ignore
                response[index]['optimizer_config_twotronics'] = item['optimizer_config_twotronics'] # type: ignore
                response[index]['scheduler_config'] = item['scheduler_config'] # type: ignore
                response[index]['scheduler_config_twotronics'] = item['scheduler_config_twotronics'] # type: ignore
                response[index]['warmup_config'] = item['warmup_config'] # type: ignore
                response[index]['server_address'] = item['server_address'] # type: ignore
                response[index]['shape'] = item['shape'] # type: ignore
                response[index]['status'] = item['status'] # type: ignore 
                response[index]['configuration_id'] = item['configuration_id'] # type: ignore
                response[index]['checked'] = item['checked'] # type: ignore
                response[index]['encryption'] = item['encryption'] # type: ignore
                arr.append(response[index])        
        return arr
        
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR',ex.args, '')
        return 'Error'
#==========================================================
#============= ORCHESTRATOR API ===========================
#==========================================================
#Get Configuration By Model Name
@app.route('/showConfigurationModel',methods = ['POST'])
def getShowConfiguration():
    try:
        data = request.get_json()
        collection = database["configuration_models"]
        config_model = collection.find_one({"model_name":data["model_name"]},{"_id":0}) 
        return make_response(jsonify( config_model), 200)
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'configurationsbyModel method')
        return make_response(jsonify({ "data": "Error to get the configuration" }), 200)

#Get Trained Model Configuration
@app.route('/recoverTrainedConfiguration',methods = ['POST'])
def getTrainedConfiguration():
    try:
        data = request.get_json()
        collection = database["configuration_models"]
        config_model = collection.find_one({"configuration_id":data['configurationId']},{"_id":0}) 
        return make_response(jsonify( config_model), 200)
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'configurationsbyModel method')
        return make_response(jsonify({ "data": "Error to get the configuration" }), 200)
#Get Persist Configuration
@app.route('/getPersistConfig', methods = ['GET'])
def getPersistConfiguration():
    try:
        collection = database['aditional_data_model']
        res = collection.find({},{'_id':0,'eval_metrics':0,'eval_metrics_twotronic':0,'num_rounds':0,'min_available_clients':0,'min_fit_clients':0,'status':0,'configuration_id':0,'checked':0,'encryption':0})
        return jsonify(list(res))
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'getPersistConfig method')
        return make_response(jsonify({ "data": "Error to get the persist configuration" }), 200)  
    
# Add a configuration for a specific model
@app.route('/storeConfigurationModel',methods = ['POST'])
def addConfigurationModel():
    try:
        exist_config = False
        configuration = request.get_json()
        collection = database['configuration_models']
        configuration_db = collection.find({},{"_id":0})

        config_ids = collection.find({},{"configuration_id":1,"_id":0})
        list_config_ids = []
        for ids in config_ids:
            list_config_ids.append(ids['configuration_id'])

        if len(configuration["stopping_target"]) != 0:
            if configuration["stopping_target"][configuration["eval_metrics"]]:
                configuration["stopping_target"][configuration["eval_metrics"]] = str(configuration["stopping_target"][configuration["eval_metrics"]])
        
        for config in configuration_db:
            if json.dumps(config,sort_keys=True) == json.dumps(configuration,sort_keys=True):
                exist_config = True
                return make_response(jsonify({ "data" : config}), 200)
            else:
                exist_config = False

        if exist_config == False:
            configuration['configuration_id'] = randint(0,100)

        while configuration['configuration_id'] in list_config_ids:
            configuration['configuration_id'] = randint(0,100)
        
        
        register = collection.insert_one(configuration)
        
        if configuration.get('_id'):
            del configuration['_id']

        if len(configuration["stopping_target"]) != 0:
            if configuration["stopping_target"][configuration["eval_metrics"]]:
                configuration["stopping_target"][configuration["eval_metrics"]] = float(configuration["stopping_target"][configuration["eval_metrics"]])
        
        return make_response(jsonify({ "data" : configuration}), 200)

    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'storeConfigurationModel method')

    return make_response(jsonify({ "data" : "Register not inserted. There is an error"}), 200)
#Recover configurations by model
@app.route('/configurationsbyModel/<id>',methods = ['GET'])
def configurationsbyModel(id):
    try:
        collection = database['configuration_models']
        configuration = collection.find({'model_name':id},{'_id':0})

        return make_response(jsonify({ "data": list(configuration) }), 200)
        
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'configurationsbyModel method')
    return make_response(jsonify({ "Error" : "There was an error during execution"}), 200)

#Recover all configurations
@app.route('/getConfigurations',methods = ['GET'])
def getConfigurations():
    try:
        collection = database['configuration_models']
        
        configuration = collection.find({},{'_id':0})

        return make_response(jsonify({ "data": list(configuration)}), 200)
        
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'configurationsbyModel method')
    return make_response(jsonify({ "Error" : "There was an error during execution"}), 200)

@app.route('/updateConfigurationModel',methods = ['POST'])
def updateConfigurationModel():
    try:
        configuration = request.get_json()

        collection = database['configuration_models']
        query = {'model_name': configuration['model_name']}

        #Delete the current register
        collection.delete_one(query)
        #Insert the new one
        
        register = collection.insert_one(configuration)


        return make_response(jsonify({ "data" : "Register updated"}), 200)
    except Exception as ex:
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, 'updateConfigurationModel method')

    return make_response(jsonify({ "data" : "Register not updated. There is an error"}), 200)

# Start training iteration 
@app.route('/trainingModel',methods = ['POST'])
def trainingModel():
    global available_ui_clients
    showMessage = None
    try:
        model = request.get_json()
        
        collection = database['configuration_models']
        configuration = collection.find_one({'configuration_id':model['configuration_id']})
        list_trainging_id = req.get(f'http://{const.FL_REPOSITORY_HOSTNAME}:{const.FL_REPOSITORY_PORT}/training-results')
        idsList = []
        res_json = list_trainging_id.json()
        if(len(res_json)>0):
            for ids in res_json:
                idsList.append(int(ids['training_id']))

            n_training_id = randint(0,100)
            while n_training_id in idsList:
                n_training_id = randint(0,100)
        else:
            n_training_id = randint(0,100)
        model['training_id'] = n_training_id
        available_ui_clients = int(configuration['min_available_clients'])
        if(len(active_connections) >= available_ui_clients):
            check = True
            configurationToTrainingCollector = sendInfoTrainingCollector(model,configuration,check)

            configurationToLocalOperation = sendInfoLocalOperation(model,configuration,check)

            logging.info(f'Configuration sending status to Local Operations: {configurationToLocalOperation}')
            logging.info(f'Configuration sending status to Training Collector: {configurationToTrainingCollector}')
            
            showMessage = False
            if configurationToLocalOperation == True and configurationToTrainingCollector == True:
                return make_response(jsonify({ "data" : "Training started. Configuration sended to Local Operation and Training Collector", 'close': True}), 200)
            else:
                showMessage = True
        else:
            check = False
            configurationToTrainingCollector = sendInfoTrainingCollector(model,configuration,check)

            configurationToLocalOperation = sendInfoLocalOperation(model,configuration,check)

    except Exception as ex:
        logging.error('Error to start the training')
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, '')

    if showMessage:
        sendNotification('ERROR', "There is an error starting the training or sending the configuration to the other enablers", '')
    return make_response(jsonify({ "data" : "There is an error starting the training or sending the configuration to the other enablers", 'close': False}), 200) 

# Recover round ended (information coming from the Training Collector)
@app.route('/FL_traininground',methods = ['POST'])
def FL_traininground():
    try:
        message = request.get_json()
        query = requests.post(f'http://{const.FL_GUI_API_HOSTNAME}:{const.FL_GUI_API_PORT}/notification', data = message)

        return make_response(jsonify({ "data" : "Message sended to the UI"}), 200)

    except Exception as ex:
        logging.error('Error to recover round ended')
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, '')

    return make_response(jsonify({ "data" : "There is an error receiving the information from the training collector"}), 200)

#Call enablers to recover its status
@app.route('/recoverStatusFromEnablers',methods = ['GET']) # type: ignore
def recoverStatusFromEnablers():
    try:
        print('Query to local operations for recovering its status')

        headers = {
            'Content-Type': 'application/json'
        }
        
        query_status_local_operation = req.post(f'http://{const.FL_LOCAL_OPERATIONS_HOSTNAME}:{const.FL_LOCAL_OPERATIONS_PORT}/job/status', headers=headers)
        print('answer status from Local Operations', query_status_local_operation.text)

        return make_response(jsonify({ "data" : "Call executed"}), 200)

    except Exception as ex:
        logging.error('Error to recover enablers status')
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, '')

@app.route("/recoverTrainingEpochs/<epoch>/<total_epochs>",methods = ['GET'])
def FL_trainingEpochs(epoch,total_epochs):
    try:
        data = 'Epochs:'+epoch+':'+total_epochs
        sendNotification('SUCCESS',data,'')
        return make_response(data, 200)
    except Exception as ex:
        logging.error('Error to receive epochs from Training')
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, '')

    return make_response(jsonify({ "data" : "There is an error receiving the information from the local operations"}), 200)

@app.route("/FL_early_end", methods = ['POST'])
def stop_f1_score():
    try:
        data = request.get_json()
        sendNotification('STOP',json.dumps(data),'Stop Early End')
        return make_response(data, 200)
    except Exception as ex:
        logging.error('Error to receive data from Early End')
        logging.error('Error: ', ex.args)
        sendNotification('ERROR', ex.args, '')
    return make_response(jsonify({ "data" : "There is an error receiving the F1 score from the Training Collector"}), 200)
async def websocket_handler(websocket,path):
    global active_connections, available_ui_clients
    try:
        while True:
            data = await websocket.recv()
            dict_data = json.loads(data)
            set_tuple = (websocket,dict_data["host"],dict_data["port"],dict_data["status"])          
            active_connections.add(set_tuple)
            set_copy = active_connections.copy()

            for websock, host,port, status in set_copy:
                if not websock.open:
                    active_connections.remove((websock,host,port,status))
            
            if len(active_connections) < int(available_ui_clients):
                message = {"status":"STOP" , "message":"Not enough Local Operations"}
                headers = {
                    'Content-Type': 'application/json'
                }
                logging.warning(f'NOT HAPPY PATH SCENARIO: {message}')
                query_training_collector = req.post(f'http://{const.FL_TRAINING_COLLECTOR_HOSTNAME}:{const.FL_TRAINING_COLLECTOR_PORT}/job/stop', headers=headers, data = json.dumps(message))
                sendNotification('STOP',json.dumps(message),'Stop Not Enough LO')
            response = "Message sended to websocket client"
            await websocket.send(response)
            
    except websockets.exceptions.ConnectionClosedOK: # type: ignore
        logging.info("Connection Closed Correctly")
    except websockets.exceptions.ConnectionClosedError as ex: # type: ignore
        logging.warning(f"Connection Closed By Error: {ex}")
        message = {"status":"STOP" , "message":"Not enough Local Operations"}
        headers = {
            'Content-Type': 'application/json'
        }
        logging.warning(f'NOT HAPPY PATH SCENARIO: {message}')
        query_training_collector = req.post(f'http://{const.FL_TRAINING_COLLECTOR_HOSTNAME}:{const.FL_TRAINING_COLLECTOR_PORT}/job/stop', headers=headers, data = json.dumps(message))
        sendNotification('STOP',json.dumps(message),'Stop Not Enough LO')

async def websocket_server():
    server = await websockets.serve(websocket_handler,'0.0.0.0', 8765,ping_interval=None) # type: ignore
    logging.info("Websocket server started in ws://localhost:8765")
    await server.wait_closed()

def start_websocket_server():
    asyncio.run(websocket_server())

def start_flask():
    app.run(host= HOST, port = PORT, threaded = True, debug = True, use_reloader = False)
#======================================
#============= MAIN ===================
#======================================
    
if __name__ == '__main__':
    ws_thread = threading.Thread(target=start_websocket_server)
    ws_thread.start()

    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exit...")
