import variables from '../utils/variables';
import request from '../utils/request_FLRepository';

export function modelsList() {
	return request({
		url: '/model',
		method: variables.METHOD_GET
	});
}

export function getAvailableModels() {
	return request({
		url: '/models/available',
		method: variables.METHOD_GET
	});
}

export function downloadModelFile2(model) {
	return request({
		url: '/models/download',
		method: variables.METHOD_POST,
		data: model,
		headers: {
			'Content-Type': variables.Application_Json,
			Accept: variables.Application_Json
		}
	})
}

export function modelShell(filename,version,configid) {
	return request({
		url: '/models/download/shell/'+filename+'/'+version+'/'+configid,
		method: variables.METHOD_GET,
	})
}

export function downloadModelFile(model) {
	return request({
		url: '/training-results/weights/'+model.model_name+'/'+model.model_version+'/'+model.training_id,
		method: variables.METHOD_GET
	})
}

export function strategiesList() {
	return request({
		url: '/strategy',
		method: variables.METHOD_GET
	});
}

export function trainingResultsList() {
	return request({
		url: '/training-results',
		method: variables.METHOD_GET
	});
}
