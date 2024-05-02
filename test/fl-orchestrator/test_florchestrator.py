import os
import sys
#SET ABSOLUTE FILE LOCATION
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir,".."))

import requests as req
import unittest
import tests.config as c
import json



class Test01_FlOrchestrator(unittest.TestCase):
    #SET ORCHESTRATOR URL
    def setUp(self):
        self.base_url = c.BASE_URL

    #HANDLING ERRORS CODE
    def errors_handling(self,response):
        if int(response.status_code) in c.INFORMATIVE_RESPONSE_STATUS:
            text = f"INFORMATIVE RESPONSE: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.INFORMATIVE_RESPONSE_STATUS[int(response.status_code)]}"
            return text,response.status_code
        elif int(response.status_code) in c.SUCCESSFUL_RESPONSE_STATUS :
            text = f"SUCCESSFUL RESPONSE: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.SUCCESSFUL_RESPONSE_STATUS[int(response.status_code)]}"
            return text,response.status_code
        elif int(response.status_code) in c.REDIRECT_RESPONSE_STATUS:
            raise TypeError(f"REDIRECT: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.REDIRECT_RESPONSE_STATUS[int(response.status_code)]}")
        elif int(response.status_code) in c.ERROR_CLIENT_RESPONSE_STATUS:
            raise TypeError(f"CLIENT ERROR: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.ERROR_CLIENT_RESPONSE_STATUS[int(response.status_code)]}")
        elif int(response.status_code) in c.ERROR_SERVER_RESPONSE_STATUS:
            raise TypeError(f"SERVER ERROR: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.ERROR_SERVER_RESPONSE_STATUS[int(response.status_code)]}")
        else:
            raise TypeError(c.DEFAULT_STATUS)

    #Insert aditional data into MongoDB    
    def test_insertAditionalModelData(self):
        response = req.get(f"{self.base_url}/addModelData")
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertEqual(bool(response.content),True)
            print("\n" ,result[0])
        except:
            print("ERROR \n" ,result[0])

    #Get Show Configuration
    def test_ShowConfiguration(self):
        response = req.post(f"{self.base_url}/showConfigurationModel",headers=c.HEADERS,data=c.SHOW_CONFIGURATION)
        result = self.errors_handling(response)
        decode = json.loads(response.content.decode('utf-8'))
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode,dict)
            self.assertTrue(len(decode)>0)
            print("\n" ,result[0])
        except:
            print("ERROR \n",result[0])

    #Get the merged data from repository and orchestrator
    def test_recoverMergedModelData(self):
        response = req.get(f"{self.base_url}/modelData")
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(json.loads(response.content.decode('utf-8')),list)
            self.assertTrue(len(json.loads(response.content.decode('utf-8'))) > 0)
            print("\n" ,result[0])
        except:
            print("ERROR \n",result[0])
    
    #Add configuration for a specific model
    def test_storeConfigurationModel(self):
        response = req.post(f"{self.base_url}/storeConfigurationModel",headers=c.HEADERS,data=c.CONFIGURATION)
        result = self.errors_handling(response)
        decode = json.loads(response.content.decode('utf-8'))
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode,dict)
            self.assertTrue(len(decode)>0)
            print("\n" ,result[0])
        except:
            print("ERROR \n",result[0])

    #Recover configuration by model
    def test_configurationsbyModel(self):
        response = req.get(f"{self.base_url}/configurationsbyModel/{c.ID_CONFIG_MODEL}")
        result = self.errors_handling(response)
        decode = json.loads(response.content.decode('utf-8'))
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode,dict)
            self.assertTrue(len(decode["data"])>0)
            print("\n" ,result[0])
        except:
            print("ERROR \n",result[0])

    #Recover all configurations
    def test_getConfigurations(self):
        response = req.get(f"{self.base_url}/getConfigurations")
        decode = json.loads(response.content.decode('utf-8'))
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode,dict)
            self.assertTrue(len(decode["data"])>0)
            print("\n" ,result[0])
        except:
           print("ERROR \n",result[0]) 

    #Update Configuration Model
    """     def test_updateConfigurationModel(self):
            response = req.post(f"{self.base_url}/updateConfigurationModel",headers=c.HEADERS,data=c.UPDATE_CONFIGURATION)
            decode = response.content.decode('utf-8')
            result = self.errors_handling(response)
            try:
                self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
                self.assertIsInstance(decode["data"],str)
                self.assertTrue(len(decode["data"])>0)
                self.assertEqual(decode["data"],c.UPDATE_RESPONSE)
                print("\n" ,result[0])
            except:
            print("ERROR \n",result[0]) 
    """
    """ #TRAIN MODEL
    def test_trainModel(self):
        response = req.post(f"{self.base_url}/trainingModel",headers=c.HEADERS,data=c.TRAIN_CONFIGURATION)
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode["data"],str)
            self.assertTrue(len(decode["data"])>0)
            self.assertEqual(decode["data"],c.TRAIN_RESPONSE)
            print("\n" ,result[0])
        except:
           print("ERROR \n",result[0]) 

    # Recover round ended (information coming from the Training Collector)
    def test_FlTraininground(self):
        response = req.post(f"{self.base_url}/FL_traininground",headers=c.HEADERS,data=c.TRAINING_ROUND_CONFIGURATION)
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode["data"],str)
            self.assertTrue(len(decode["data"])>0)
            self.assertEqual(decode["data"],c.TRAINING_ROUND_RESPONSE)
            print("\n" ,result[0])
        except:
           print("ERROR \n",result[0]) 

    # Call enablers to recover its status
    def test_RecoverStatusFromEnablers(self):
        response = req.get(f"{self.base_url}/recoverStatusFromEnablers")
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode["data"],str)
            self.assertTrue(len(decode["data"])>0)
            self.assertEqual(decode["data"],c.STATUS_ENABLER_RESPONSE)
            print("\n" ,result[0])
        except:
           print("ERROR \n",result[0]) 

    #Recover Epochs Status
    def test_RecoverTrainingEpochs(self):
        response = req.get(f"{self.base_url}/recoverTrainingEpochs/{str(c.EPOCHS)}/{str(c.TOTAL_EPOCHS)}")
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode,str)
            self.assertTrue(len(decode)>0)
            self.assertEqual(decode,c.EPOCHS_RESPONSE)
            print("\n" ,result[0])
        except:
           print("ERROR EPOCHS \n",result[0])  """
        
class Test02_FlOrchestrator(unittest.TestCase):
    #SET ORCHESTRATOR URL
    def setUp(self):
        self.base_url = c.BASE_URL

    #HANDLING ERRORS CODE
    def errors_handling(self,response):
        if int(response.status_code) in c.INFORMATIVE_RESPONSE_STATUS:
            text = f"INFORMATIVE RESPONSE: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.INFORMATIVE_RESPONSE_STATUS[int(response.status_code)]}"
            return text,response.status_code
        elif int(response.status_code) in c.SUCCESSFUL_RESPONSE_STATUS :
            text = f"SUCCESSFUL RESPONSE: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.SUCCESSFUL_RESPONSE_STATUS[int(response.status_code)]}"
            return text,response.status_code
        elif int(response.status_code) in c.REDIRECT_RESPONSE_STATUS:
            raise TypeError(f"REDIRECT: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.REDIRECT_RESPONSE_STATUS[int(response.status_code)]}")
        elif int(response.status_code) in c.ERROR_CLIENT_RESPONSE_STATUS:
            raise TypeError(f"CLIENT ERROR: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.ERROR_CLIENT_RESPONSE_STATUS[int(response.status_code)]}")
        elif int(response.status_code) in c.ERROR_SERVER_RESPONSE_STATUS:
            raise TypeError(f"SERVER ERROR: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.ERROR_SERVER_RESPONSE_STATUS[int(response.status_code)]}")
        else:
            raise TypeError(c.DEFAULT_STATUS)

    #TRAIN MODEL
    def test_trainModel(self):
        response = req.post(f"{self.base_url}/trainingModel",headers=c.HEADERS,data=c.TRAIN_CONFIGURATION)
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode["data"],str)
            self.assertTrue(len(decode["data"])>0)
            self.assertEqual(decode["data"],c.TRAIN_RESPONSE)
            print("\n" ,result[0])
        except:
           print("ERROR \n",result[0]) 
    
class Test03_FlOrchestrator(unittest.TestCase):
    #SET ORCHESTRATOR URL
    def setUp(self):
        self.base_url = c.BASE_URL

    #HANDLING ERRORS CODE
    def errors_handling(self,response):
        if int(response.status_code) in c.INFORMATIVE_RESPONSE_STATUS:
            text = f"INFORMATIVE RESPONSE: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.INFORMATIVE_RESPONSE_STATUS[int(response.status_code)]}"
            return text,response.status_code
        elif int(response.status_code) in c.SUCCESSFUL_RESPONSE_STATUS :
            text = f"SUCCESSFUL RESPONSE: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.SUCCESSFUL_RESPONSE_STATUS[int(response.status_code)]}"
            return text,response.status_code
        elif int(response.status_code) in c.REDIRECT_RESPONSE_STATUS:
            raise TypeError(f"REDIRECT: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.REDIRECT_RESPONSE_STATUS[int(response.status_code)]}")
        elif int(response.status_code) in c.ERROR_CLIENT_RESPONSE_STATUS:
            raise TypeError(f"CLIENT ERROR: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.ERROR_CLIENT_RESPONSE_STATUS[int(response.status_code)]}")
        elif int(response.status_code) in c.ERROR_SERVER_RESPONSE_STATUS:
            raise TypeError(f"SERVER ERROR: \n STATUS CODE: {response.status_code}\n DESCRIPTION: {c.ERROR_SERVER_RESPONSE_STATUS[int(response.status_code)]}")
        else:
            raise TypeError(c.DEFAULT_STATUS)

    # Recover round ended (information coming from the Training Collector)
    def test_FlTraininground(self):
        response = req.post(f"{self.base_url}/FL_traininground",headers=c.HEADERS,data=c.TRAINING_ROUND_CONFIGURATION)
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode["data"],str)
            self.assertTrue(len(decode["data"])>0)
            self.assertEqual(decode["data"],c.TRAINING_ROUND_RESPONSE)
            print("\n" ,result[0])
        except:
            print("ERROR \n",result[0]) 

    # Call enablers to recover its status
    def test_RecoverStatusFromEnablers(self):
        response = req.get(f"{self.base_url}/recoverStatusFromEnablers")
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode["data"],str)
            self.assertTrue(len(decode["data"])>0)
            self.assertEqual(decode["data"],c.STATUS_ENABLER_RESPONSE)
            print("\n" ,result[0])
        except:
            print("ERROR \n",result[0]) 

    #Recover Epochs Status
    def test_RecoverTrainingEpochs(self):
        response = req.get(f"{self.base_url}/recoverTrainingEpochs/{str(c.EPOCHS)}/{str(c.TOTAL_EPOCHS)}")
        decode = response.content.decode('utf-8')
        result = self.errors_handling(response)
        try:
            self.assertTrue(int(result[1]) in c.SUCCESSFUL_RESPONSE_STATUS or int(result[1]) in c.INFORMATIVE_RESPONSE_STATUS)
            self.assertIsInstance(decode,str)
            self.assertTrue(len(decode)>0)
            self.assertEqual(decode,c.EPOCHS_RESPONSE)
            print("\n" ,result[0])
        except:
            print("ERROR EPOCHS \n",result[0])

if __name__ == '__main__':
    unittest.main()