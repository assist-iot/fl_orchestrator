# FL Orchestrator GUI Documentation Page 

## Introduction

**FL Orchestrator** is one of the enablers developed in the context of the **FL Architecture** of the [ASSIST-IoT project](https://assist-iot.eu/).

FL Orchestrator is responsible of specifying details of FL workflow(s)/pipeline(s). Among these details or features are:  

- FL job scheduling  
- Manage the FL life cycle  
- Selecting and delivering initial version(s) of the shared algorithm  
- Delivering the version(s) of modules used in various stages of the process, such as training stopping criteria  
- Handling the different "error conditions" that may occur during the FL process

## Place in the architecture

Next picture depicts the FL architecture

![FL Architecture](doc/images/fl_architecture.png "FL Architecture")

It is in the centre of the image. It is the core element of the architecture and is responsible for initiating the different iterations of model training.

## User guide

In order to manage the training of the models in a simple way, an interface has been developed to start the training rounds of the different models available in the FL Repository.

This is how it looks like.

![Web Application](doc/images/UI_appearance.PNG "Web Application")

This is the meaning of the numbers shown in the picture:

- **1**. List of models retrieved from the FL Repository.
- **2**. Reload the list of models.
- **3**. Option that allows filtering by the modelName field to search for a model from those retrieved from the FL Repository.

The **Actions** colummn includes these functionalities:

- **View model**. Displays the JSON of the model. It can be seen in the following picture.

![View model functionality](doc/images/View_model.PNG "View model functionality")

- **Edit model**. Displays a form to insert/update the training configuration of the selected model. The following picture depicts the appearance of this form.

![Edit model functionality](doc/images/Edit_model.PNG "Edit model functionality")

Taking these functionalities into account, the steps to start a training round are as follows:

- Select one of the models from the list retrieved from the FL Repository.

![Model Selected](doc/images/model_selected.png "Model selected")

- Verify that a configuration exists for the selected model. If we pass over the Train model button and it appears disabled, it is because there is no configuration, So, the next step is to register one going to the Edit model option. Once the configuration has been saved, click on the Train model button. If the Train model is enabled, click on this option for start the training.

- Click over the Train model button will show this form to confirm that will start the training for the model selected.

![Train model](doc/images/Train_model.PNG "Train model")

Once the user clicks over the Start button the training starts. UI will receive updates each time a round finishes.

## Prerequisites

The main prerequisites are the installation of [Docker](https://docs.docker.com/get-started/overview/) and [Docker-compose](https://docs.docker.com/compose/).

The following links provide information on how to install [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) and [Docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04).

These prerequisites are necessary in case of running the enabler as a container (**Docker**). However, it is also possible to run the component independently. In this case, it's mandatory to have Python installed on the machine where the Orchestrator will be executed. At least version 3.8 is recommended (this is the version of the Python image being used). It is also necessary to install some additinal libraries or packages. These additional packages can be seen in the requirements.txt file (inside the orchestrator folder).

The following image illustrates the libraries needed for the orchestrator.

![Requirements.txt file](doc/images/requirements.PNG "Additional pacckages in the requirements.txt file")

## Installation with docker

```
docker compose up -d
```

## Verification

FL Orchestrator and the other enablers have been conceived as APIs that will have methods that interact with each other.

Therefore, the best to verify their correct deployment and operation is to test these APIs.

FL Orchestrator has a [Swagger](https://swagger.io/docs/specification/2-0/what-is-swagger/) that allows to test all its methods. This swagger is deployed at the following URL: http://localhost:5000/api/docs

Next picture shows the appearance of the swagger and its methods.

![FL Orchestrator Swagger](doc/images/fl_orchestrator_swagger.PNG "Swagger for the FL Orchestrator")

Expanding the method area (/getConfigurations) in our case. The Execute option appears. Clicking on this button and if the method has the required parameters, the result code is obtained (200, in case it has gone well). Also in the [curl](https://curl.se/) area, it is possible to see the request that would be made to execute this method externally. In the Response body area it is possible to see the result, the list of the configurations that currently are stored in the FL Orchestrator.

Next picture depicts what has been explained in the previous paragraph. The areas **code**, **curl** and **Response body** are highlight.

![Testing Swagger](doc/images/testing_swagger.png "Testing models method of FL Orchestrator API")

## Building the Docker images

```
docker compose build
```
## Deploying FL Orchestrator GUI Helm chart with Kubernetes and Helm3 

The FL Orchestrator and FL GUI, are in the public repository in assist-public-repo/fl-orchestrator-gui
[enablers-registry / public · GitLab (assist-iot.eu)](https://gitlab.assist-iot.eu/enablers-registry/public)

1. Create a Secret to access Assist-iot's private container registry
```bash
kubectl create secret docker-registry regcred --docker-server=https://gitlab.assist-iot.eu:5050/ --docker-username=<your-name> --docker-password=<your-pword/token> --docker-email=<your-email>
```
2. Deploy dependencies
  - FL-Localoperations: https://gitlab.assist-iot.eu/wp5/t52/fl-local-operations
  - FL-Training Collector KPI enabler: https://gitlab.assist-iot.eu/wp5/t52/fl-training-collector
  - FL-Respository KPI enabler: https://gitlab.assist-iot.eu/wp5/t52/fl-repository

3. Deploy helm chart from the command line

To deploy it from the command line you will need to set the  flag -f with a custom_values.yaml file according to your configuration. Here is an example

```bash
helm install fl-orchestrator-gui assist-public-repo/fl-orchestrator-gui -f /opt/assist/fl/fl-orchestrator-and-fl-gui/custom_values.yaml
```

```yml
orchestrator:
  envVars:
    FL_REPOSITORY_HOSTNAME: flrepositorylocaldb-flrepositorydb-flrepository
    FL_REPOSITORY_PORT: 9012

    FL_REPOSITORY_DB_HOSTNAME: flrepositorylocaldb-flrepositorydb-flrepositorydb 
    FL_LOCAL_OPERATIONS_HOSTNAME: fllocaloperationslocal-trainingapp
    FL_LOCAL_OPERATIONS_PORT: 9050
    FL_TRAINING_COLLECTOR_HOSTNAME: trainingcollectorlocal-trainingmain
    FL_TRAINING_COLLECTOR_PORT: 8000 

webapp:
  envVars:
    FL_GUI_API_HOST_NAME: "localhost"
    FL_GUI_API_PORT: 31000
    FL_GUI_API_WS_PORT: 31010

dbmongo:
  image:
    repository: gitlab.assist-iot.eu:5050/enablers-registry/public/fl-orchestrator-gui/fl-db-mongo-4
    tag: "latest"
```

In the example you can see an example configuration, which is the default one, but in your case you should update it for the host where it is deployed and the dependencies of the other FLs.

Other helm commands

```bash
# Get all release
helm list

#Delete release
helm uninstall <name-release>

```

4. Deploy helm chart from SmartOrchestrator/Manageability

If you have the **SmartOrchestrator you can open the Manageability** WebApp and deploy it more easily, adding a json object the configuration with parameters that you need for your environment.


```json
{
  "orchestrator": {
    "envVars": {
      "FL_REPOSITORY_HOSTNAME": "flrepositorylocaldb-flrepositorydb-flrepository",
      "FL_REPOSITORY_PORT": 9012,
      "FL_REPOSITORY_DB_HOSTNAME": "flrepositorylocaldb-flrepositorydb-flrepositorydb",
      "FL_LOCAL_OPERATIONS_HOSTNAME": "fllocaloperationslocal-trainingapp",
      "FL_LOCAL_OPERATIONS_PORT": 9050,
      "FL_TRAINING_COLLECTOR_HOSTNAME": "trainingcollectorlocal-trainingmain",
      "FL_TRAINING_COLLECTOR_PORT": 8000
    }
  },
  "webapp": {
    "envVars": {
      "FL_GUI_API_HOST_NAME": "localhost",
      "FL_GUI_API_PORT": 31000,
      "FL_GUI_API_WS_PORT": 31010
    }
  },
  "dbmongo": {
    "image": {
      "repository": "gitlab.assist-iot.eu:5050/enablers-registry/public/fl-orchestrator-gui/fl-db-mongo-4",
      "tag": "latest"
    }
  }
}
```

![Manageability custom values example](doc/images/manageability_01.png "Manageability custom values example")
![Manageability custom values example](doc/images/manageability_01.png "Manageability custom values example")

Once deployed, the interface is easy to use. In this video you can see it. https://youtu.be/9k1Okt7__Tg?si=ycO643pNf8ibKQtf

## Version control and release

The table of this section it is a software release overview of the different elements for the orchestrator's enabler. The division has been made on the basis of the different files (or folders) needed to execute the component. This is shown in the following figure.

![Components](doc/images/components.PNG "Division of elements for executing the orchestrator")

| File Name / Folder  | Description  | Language |
| :------------ |:--------------- | :----- |
| docker-compose.yml | Docker compose file responsible for launching the services needed for the orchestrator | [YAML](https://en.wikipedia.org/wiki/YAML) |
| orchestrator | Folder containing the scripts needed to run the orchestrator service. It also contains the files and folders necessary to be able to deploy a swagger of the component | Python, YAML, [CSS](https://www.w3schools.com/css/css_intro.asp), [HTML](https://www.w3schools.com/html/html_intro.asp), [JavaScript](https://www.w3schools.com/whatis/whatis_js.asp), [JSON](https://www.w3schools.com/js/js_json_intro.asp) |

## License

> **To be completed**

## Notice (dependencies)

> **To be completed**

`$ npm install marked`
