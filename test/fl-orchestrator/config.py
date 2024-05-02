BASE_URL = "http://localhost:5000"
#REQUEST INFO
HEADERS = {
    'Content-Type': 'application/json',
    'Accept' : 'application/json'
}

#SHOW CONFIGURATION
SHOW_CONFIGURATION = {"model_name":"keras_test"}
#STORE DATA CONFIGURATION
CONFIGURATION = {
"configuration_id":33,
"eval_metrics":"accuracy",
"eval_metrics_value":"0",
"min_available_clients": "1",
"min_fit_clients":"1",
"model_name": "keras_test",
"number_of_rounds": "15",
"privacy-mechanisms":{},
"strategy": "fedavg"
}
#ID CONFIGURATION BY MODEL
ID_CONFIG_MODEL = "keras_test"
#UPDATE MODEL CONFIGURATION
""" UPDATE_CONFIGURATION = {}
UPDATE_RESPONSE = "Register updated" """
#TRAIN MODEL
TRAIN_CONFIGURATION ={'adapt_config': 'base', 'checked': True, 'client_type_id': 'local1', 'config': [{'batch_size': '64', 'config_id': 'min_effort', 'epochs': '1', 'learning_rate': '0.001', 'steps_per_epoch': '32'}], 'configuration_id': 32, 'encryption': ['homomorphic', 'dp-adaptive'], 'eval_func': 'categorical_crossentropy', 'eval_metrics': ['accuracy'], 'meta': {'library': 'keras'}, 'min_available_clients': 8, 'min_fit_clients': 8, 'model_id': '6424597f48890c9dadfadecb', 'model_name': 'keras_test', 'model_version': 'version_1', 'num_classes': 10, 'num_rounds': 15, 'optimizer_config': {'amsgrad': 'True', 'learning_rate': '0.005', 'optimizer': 'adam'}, 'scheduler_config': {'factor': '0.5', 'min_delta': '0.0003', 'scheduler': 'reducelronplateau'}, 'server_address': 'trainingcollectorlocal-trainingmain-svc2', 'shape': [32, 32, 3], 'status': 'running', 'warmup_config': {'scheduler': 'lambdalr', 'scheduler_conf': {'scheduler': 'lambdalr'}, 'warmup_epochs': '1', 'warmup_factor': '0.001', 'warmup_iters': '1000'}, 'strategy': 'fedavg'}
TRAIN_RESPONSE = "Training started. Configuration sended to Local Operation and Training Collector"
#TRAINING ROUND
TRAINING_ROUND_CONFIGURATION = {"test":"sended"}
TRAINING_ROUND_RESPONSE = "Message sended to the UI"
#RECOVER STATUS FROM ENABLERS
STATUS_ENABLER_RESPONSE = "Call executed"
#RECOVER TRAINING EPOCHS
EPOCHS = 1
TOTAL_EPOCHS = 5
EPOCHS_RESPONSE = f"Epochs:{str(EPOCHS)}:{str(TOTAL_EPOCHS)}"


#STATUS ERRORS DESCRIPTIONS
DEFAULT_STATUS = "Another error has been found for which information could not be obtained"
INFORMATIVE_RESPONSE_STATUS = {
    100:"Continue: Everything so far is fine and the client should continue with the request or ignore it if it is already done.",
    101:"Switching Protocol: Sending response to an Upgrade request header by the client and indicates that the server accepts the protocol change proposed by the user agent.",
    102:"Processing: The server has received the request and is still processing it, so no response is available.",
    103:"Early Hints: The user agent can start prefetching resources while the server prepares a response.",
}
SUCCESSFUL_RESPONSE_STATUS = {
    200:"OK: The request has been successful.",
    201:"Created: The request has been successful and a new resource has been created as a result of it.",
    202:"Accepted: The request has been received, but no action has yet been taken.",
    203:"Non-Authoritative Information: The request has been completed successfully, but its content has not been obtained from the original source requested.",
    204:"No Content: The request has been completed successfully but your response has no content.",
    205:"Reset Content: The request has been completed successfully, but its response contains no content and also the user agent has to initialize the page from which the request was made.",
    206:"Partial Content: The request will partially serve the requested content.",
    207:"Multi-Status: Conveys information about various resources where various status codes might be appropriate.",
    208:"Multi-Status: The listing of DAV elements has already been notified previously, so they will not be listed again.",
    226:"IM Used: The server has fulfilled the GET request for the resource, and the response is a representation of the result of one or more instance manipulations applied to the current instance.",
}
REDIRECT_RESPONSE_STATUS = {
    300:"Multiple Choice: This request has more than one possible response. User-Agent or the user must choose one of them.",
    301:"Moved Permanently: The URI of the requested resource has been changed. A new URI will probably be returned in the response.",
    302:"Found: The requested URI resource has been temporarily changed. New URI changes will be added in the future.",
    303:"See Other: The server sent this response to direct the client to a new resource requested at another address using a GET request.",
    304:"Not Modified: Indicates to the client that the response has not been modified.",
    305:"Use Proxy: The requested response must be accessed from a proxy.",
    307:"Temporary Redirect: Redirect the client to get the requested resource to another URI with the same method that was used in the previous request",
    308:"Permanent Redirect: The resource is now permanently located at a different URI, specified by the Location: HTTP header response.",
}
ERROR_CLIENT_RESPONSE_STATUS = {
    400:"Bad Request: The server could not interpret the request due to invalid syntax.",
    401:"Unauthorized: Authentication is required to get the requested response.",
    403:"Forbidden: The client does not have the necessary permissions.",
    404:"Not Found: The server could not find the requested content.",
    405:"Method Not Allowed: The requested method is known to the server but has been disabled and cannot be used.",
    406:"Not Acceptable: The server does not find any content following the criteria given by the user.",
    407:"Proxy Authentication Required: Authentication must be done through a proxy.",
    408:"Request Timeout: The server wants to disconnect this unused connection.",
    409:"Conflict: A request conflicts with the current state of the server.",
    410:"Gone: The requested content has been deleted from the server.",
    411:"Length Required: The server rejects the request because the Content-Length header field is not defined and the server requires it.",
    412:"Precondition Failed: The client has indicated preconditions in its headers which the server does not meet.",
    413:"Payload Too Large: The request entity is longer than the limits defined by the server.",
    414:"URI Too Long: The URI requested by the client is longer than the server is willing to interpret.",
    415:"Unsupported Media Type: The multimedia format of the requested data is not supported by the server.",
    416:"Requested Range Not Satisfiable: The range specified by the Range header field in the request does not match.",
    417:"Expectation Failed: The expectation indicated by the requested Expect header field cannot be fulfilled by the server.",
    421:"Misdirected Request: The request was directed to a server that is not capable of producing a response.",
    422:"Unprocessable Entity: The request was well-formed but could not be followed due to semantic errors.",
    423:"Locked: The resource being accessed is locked.",
    424:"Failed Dependency: The request failed due to a failure of a previous request.",
    426:"Upgrade Required: The server refuses to apply the request using the current protocol but may be willing to do so after the client upgrades to a different protocol.",
    428:"Precondition Required: The origin server requires that the request be conditional.",
    429:"Too Many Requests: Excessive requests have been submitted in a given period of time.",
    431:"Request Header Fields Too Large: The server is not willing to process the request because the header fields are too long.",
    451:"Unavailable For Legal Reasons: An illegal resource has been requested",
}
ERROR_SERVER_RESPONSE_STATUS = {
    500:"Internal Server Error: The server has encountered a situation that it does not know how to handle.",
    501:"Not Implemented: The requested method is not supported by the server and cannot be handled.",
    502:"Bad Gateway: The server got an invalid response.",
    503:"Service Unavailable: The server is not ready to handle the request.",
    504:"Gateway Timeout: The server cannot get a response in time.",
    505:"HTTP Version Not Supported: The HTTP version used in the request is not supported by the server.",
    506:"Variant Also Negotiates: The server has an internal configuration error: transparent content negotiation for the request results in a circular reference.",
    507:"Insufficient Storage: The server has an internal configuration error: the chosen resource variable is configured to couple the transparent content negotiation itself, and is therefore not a proper end point for the negotiation process.",
    508:"Loop Detected: The server encountered an infinite loop while processing the request.",
    510:"Not Extended: Additional extensions to the request are required for the server to honor them.",
    511:"Network Authentication Required: The client needs to authenticate to gain access to the network."
}

