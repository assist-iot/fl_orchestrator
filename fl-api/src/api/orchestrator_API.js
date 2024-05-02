import variables from '../utils/variables';
import request from '../utils/request_FLOrchestrator';

export function storeConfigurationModel(configuration) {
	return request({
		url: '/storeConfigurationModel',
		method: variables.METHOD_POST,
		data: configuration,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	});
}
export function recoverTrainedConfiguration(configuration) {
	return request({
		url: '/recoverTrainedConfiguration',
		method: variables.METHOD_POST,
		data: configuration,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	});
}
export function showConfigurationByModel(data) {
	return request({
		url: '/showConfigurationModel',
		method: variables.METHOD_POST,
		data: data,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	});
}
export function persistConfiguration() {
	return request({
		url: '/getPersistConfig',
		method: variables.METHOD_GET,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	});
}
export function configurationsbyModel(modelName) {
	return request({
		url: '/configurationsbyModel/' + modelName,
		method: variables.METHOD_GET
	});
}

export function updateConfigurationModel(configuration) {
	return request({
		url: '/updateConfigurationModel',
		method: variables.METHOD_POST,
		data: configuration,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	});
}

export function startTrainingIteration(model) {
	return request({
		url: '/trainingModel',
		method: variables.METHOD_POST,
		data: model,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	});
}

export function recoverStatusFromEnablers() {
	return request({
		url: '/recoverStatusFromEnablers',
		method: variables.METHOD_GET
	});
}

export function insertAditionalModelData() {
	return request({
		url: '/addModelData',
		method: variables.METHOD_GET
	});
}

export function recoverModelData(){
	return request({
		url: '/modelData',
		method: variables.METHOD_GET
	});
}
