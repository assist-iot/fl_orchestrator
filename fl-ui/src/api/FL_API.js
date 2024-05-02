import request from '@/utils/request_FL'
import constants from '../utils/constants'

/* export function getModelsList() {
  return request({
    url: '/repository/getModels',
    method: constants.METHOD_GET
  })
} */
export function getPersistConfiguration(data) {
  return request({
    url: '/orchestrator/persistConfiguration',
    method: constants.METHOD_GET
  })
}

export function getShowConfiguration(data) {
  return request({
    url: '/orchestrator/showConfiguration',
    method: constants.METHOD_POST,
    data: data,
    headers: {
      'Content-Type': constants.Application_Json,
      Accept: constants.Application_Json
    }
  })
}

export function getModelsList() {
  return request({
    url: '/orchestrator/modelData',
    method: constants.METHOD_GET
  })
}

export function loadModelData() {
  return request({
    url: '/orchestrator/loadModelData',
    method: constants.METHOD_GET
  })
}
export function modelConfiguration(data) {
  return request({
    url: '/orchestrator/modelConfiguration',
    method: constants.METHOD_POST,
    data: data,
    headers: {
      'Content-Type': constants.Application_Json,
      Accept: constants.Application_Json
    }
  })
}

export function configurationByModel(modelName) {
  return request({
    url: '/orchestrator/configurationByModel/' + modelName,
    method: constants.METHOD_GET
  })
}

export function updateConfiguration(data) {
  return request({
    url: '/orchestrator/updateConfiguration',
    method: constants.METHOD_POST,
    data: data,
    headers: {
      'Content-Type': constants.Application_Json,
      Accept: constants.Application_Json
    }
  })
}

export function startTrainingModel(model) {
  return request({
    url: '/orchestrator/startTrainingModel',
    method: constants.METHOD_POST,
    data: model,
    headers: {
      'Content-Type': constants.Application_Json,
      Accept: constants.Application_Json
    }
  })
}

export function callEnablers() {
  return request({
    url: '/orchestrator/callEnablers',
    method: constants.METHOD_GET
  })
}
export function trainedConfiguration2(configurationId) {
  return request({
    url: '/orchestrator/trainedConfiguration',
    method: constants.METHOD_POST,
    data: configurationId,
    headers: {
      'Content-Type': constants.Application_Json,
      Accept: constants.Application_Json
    }
  })
}
export function trainedConfiguration() {
  return request({
    url: '/repository/training-results',
    method: constants.METHOD_GET
  })
}
export function getAvailablesModels() {
  return request({
    url: '/repository/availableModels/',
    method: constants.METHOD_GET
  })
}

export function downloadModel(model) {
  return request({
    url: '/repository/downloadModel',
    method: constants.METHOD_POST,
    data: model,
    headers: {
      'Content-Type': constants.Application_Json,
      Accept: constants.Application_Json
    }
  })
}

export function modelShell(filename, fileversion, configid) {
  return request({
    url: '/repository/shell/model/' + filename + '/' + fileversion + '/' + configid,
    method: constants.METHOD_GET
  })
}

export function getStrategies() {
  return request({
    url: '/repository/getStrategy',
    method: constants.METHOD_GET
  })
}
