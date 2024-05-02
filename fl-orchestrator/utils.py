import requests
import os
from constants import *

from flask import jsonify, make_response

def sendNotification(notificationType, message_or_errorDescription, additional_message):

    try:

        data = {
            "id": ENABLER_NAME,
            "type": notificationType,
            "message": message_or_errorDescription,
            "additionalInfo":additional_message
        }

        #headers = {
        #    'Accept': 'application/json',
        #    'Content-Type': 'application/json'
        #}

        #This line is for Windows deployment using docker
        #query = requests.post("http://host.docker.internal:1885/notification", data = data)
        #Windows deployment
        #headers=headers, 
        query = requests.post(f"http://{FL_GUI_API_HOSTNAME}:{FL_GUI_API_PORT}/notification/errorNotification", data = data)

        return make_response(jsonify({ "data" : "Message sended to the UI" }), 200)
        
        #extracting response text
        #response = query.text
        #print('response: ', response)

    except Exception as ex:
        print('ERROR: sendNotification')
        print('ERROR: ',ex.args)
