import { modelsList, getAvailableModels, downloadModelFile, modelShell, strategiesList,trainingResultsList } from '../api/repository_API';

import CustomError from '../utils/CustomError';

const service = {};

service.getModels = getModels;
service.availableModels = availableModels;
service.downloadModel = downloadModel;
service.getShellModel = getShellModel;
service.getStrategies = getStrategies;
service.trainingResults = trainingResults;

export default service;

// Implementation
async function getModels() {
	let data = [];
	try {
		await modelsList().then(response => {
			data = response;
		});
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function availableModels() {
	let data = null;
	try {
		data = await getAvailableModels()
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function downloadModel(model){
	let data = null; 
	try{
		data = await downloadModelFile(model)
	}catch (error) {
		throw new CustomError(error.response.data, error.response.status)
	}
	return data
}

async function getShellModel(filename,version,configid){
	let data = null; 
	try{
		data = await modelShell(filename,version,configid)
	}catch (error) {
		throw new CustomError(error.response.data, error.response.status)
	}
	return data
}

async function getStrategies() {
	let data = [];
	try {
		await strategiesList().then(response => {
			data = response;
		});
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function trainingResults() {
	let data = [];
	try {
		await trainingResultsList().then(response => {
			data = response;
		});
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}
