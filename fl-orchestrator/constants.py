#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

HOST = '0.0.0.0'
PORT = 5000
ENABLER_NAME = 'ORCHESTRATOR'
TRAINING_COLLECTOR_ADDRESS = 'http://training_collector:8000'
LOCAL_OPERATIONS_ADDRESS = 'http://appv0-local_operations-1'

DB_HOST_NAME = os.getenv('DB_HOST_NAME') if  os.getenv('DB_HOST_NAME') else '0.0.0.0'
DB_PORT = os.getenv('DB_PORT') if  os.getenv('DB_PORT') else '27040'

FL_REPOSITORY_HOSTNAME = os.getenv('FL_REPOSITORY_HOSTNAME') if  os.getenv('FL_REPOSITORY_HOSTNAME') else 'localhost'
FL_REPOSITORY_PORT = os.getenv('FL_REPOSITORY_PORT') if  os.getenv('FL_REPOSITORY_PORT') else '30580'
FL_REPOSITORY_DB_HOSTNAME = os.getenv('FL_REPOSITORY_DB_HOSTNAME') if  os.getenv('FL_REPOSITORY_DB_HOSTNAME') else 'localhost'

FL_LOCAL_OPERATIONS_HOSTNAME = os.getenv('FL_LOCAL_OPERATIONS_HOSTNAME') if  os.getenv('FL_LOCAL_OPERATIONS_HOSTNAME') else 'localhost'
FL_LOCAL_OPERATIONS_PORT = os.getenv('FL_LOCAL_OPERATIONS_PORT') if  os.getenv('FL_LOCAL_OPERATIONS_PORT') else '32766'

FL_TRAINING_COLLECTOR_HOSTNAME = os.getenv('FL_TRAINING_COLLECTOR_HOSTNAME') if  os.getenv('FL_TRAINING_COLLECTOR_HOSTNAME') else 'localhost'
FL_TRAINING_COLLECTOR_PORT = os.getenv('FL_TRAINING_COLLECTOR_PORT') if  os.getenv('FL_TRAINING_COLLECTOR_PORT') else '30800'

FL_GUI_API_HOSTNAME = os.getenv('FL_GUI_API_HOSTNAME') if  os.getenv('FL_GUI_API_HOSTNAME') else 'localhost'
FL_GUI_API_PORT = os.getenv('FL_GUI_API_PORT') if  os.getenv('FL_GUI_API_PORT') else '3000'

NOT_HAPPY_SCENARIO_MESSAGE = 'The number of available clients is less than the required number of clients'
DATA_INSERT = {
  "client_type_id": "local1",  
  "server_address": "trainingcollectorlocal-trainingmain-svc2",
  "eval_metrics": [
    "accuracy"
  ],
  "eval_metrics_twotronics": [
    "accuracy","recall"
  ],
  "eval_func": "categorical_crossentropy",
  "num_classes": 10,
  "num_rounds": 15,
  "shape": [
    32,32,3
  ],
  "config": [
    {
      "config_id": "min_effort",
      "batch_size": "64",
      "steps_per_epoch": "32",
      "epochs": "1",
      "learning_rate": "0.001"
    }
  ],
  "optimizer_config": {
    "optimizer": "adam",
    "learning_rate": "0.005",
    "amsgrad": "True"
  },
  "optimizer_config_twotronics": {
    "optimizer": "sgd",
    "lr": "0.005",
    "momentum": "0.9",
    "weight_decay": "0.0005"
  },
  "scheduler_config": {
    "scheduler": "reducelronplateau",
    "factor": "0.5",
    "min_delta": "0.0003"
  },  
  "scheduler_config_twotronics": {
    "scheduler": "steplr",
    "step_size": "3",
    "gamma": "0.1"
  }, 
  "adapt_config": "base",
  "min_eval_clients":1,
  "min_available_clients": 8,
  "min_fit_clients": 8,
  "warmup_config": {
    "scheduler": "lambdalr",
    "warmup_iters": "1000",
    "warmup_epochs": "1",
    "warmup_factor": "0.001",
    "scheduler_conf": {
      "scheduler": "lambdalr"
    }
  },


  "status": "running",
  "configuration_id": 0,
  "checked": "true",
  "encryption": [
    "homomorphic",
    "dp-adaptive"
  ]
}