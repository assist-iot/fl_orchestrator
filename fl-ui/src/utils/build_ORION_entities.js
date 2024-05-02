import dataportsConstants from '../utils/constants'

export function buildAgentImage(imageID, imageName, dataSourceID) {
  	var AgentImage = {

    'id': 'urn:ngsi-ld:AgentImage:' + imageID,
    'type': dataportsConstants.AGENT_IMAGE,
    'name': {
      'type': 'Text',
      'value': imageName
    },
    'agentType': {
      'type': 'Text',
      'value': dataportsConstants.ON_DEMAND
    },
    'accessURL': {
      'type': 'Text',
      'value': dataportsConstants.baseURL_API_ON_DEMAND
    	},
    'refDataSource': {
      'type': 'Relationship',
      'value': dataSourceID
    }
  	}

  return AgentImage
}

export function buildAgentContainer(imageID, imageName, dataSourceID, containerID) {
  var AgentContainer = {

	  'id': 'urn:ngsi-ld:AgentContainer:' + containerID,
	  'type': dataportsConstants.AGENT_CONTAINER,
	  'name': {
		  'type': 'Text',
		  'value': imageName
	  },
	  'agentType': {
		  'type': 'Text',
		  'value': dataportsConstants.PUBLISH_SUBSCRIBE
	  },
	  'refDataSource': {
		  'type': 'Relationship',
		  'value': dataSourceID
	  }
  }

  return AgentContainer
}

