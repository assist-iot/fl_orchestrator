import { persistConfiguration,storeConfigurationModel,showConfigurationByModel, configurationsbyModel,recoverTrainedConfiguration, updateConfigurationModel, startTrainingIteration, recoverStatusFromEnablers, insertAditionalModelData, recoverModelData } from '../api/orchestrator_API';

import CustomError from '../utils/CustomError';

const service = {};

service.modelConfiguration = modelConfiguration;
service.configurationModel = configurationModel;
service.updateConfiguration = updateConfiguration;
service.startTrainingModel = startTrainingModel;
service.callEnablers = callEnablers;
service.loadModelData = loadModelData;
service.modelData = modelData;
service.showConfiguration = showConfiguration;
service.persistConfig = persistConfig;
service.trainedConfiguration = trainedConfiguration;
export default service;

// Implementation
async function modelConfiguration(configuration) {
	let data = null;
	try {
		data = await storeConfigurationModel(configuration)
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}
async function trainedConfiguration(configuration) {
	let data = null;
	try {
		data = await recoverTrainedConfiguration(configuration)
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}
async function showConfiguration(conf) {
	let data = null;
	try {
		data = await showConfigurationByModel(conf)
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}
async function persistConfig() {
	let data = null;
	try {
		data = await persistConfiguration()
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}
async function configurationModel(modelName) {
	let data = null;
	try {
		data = await configurationsbyModel(modelName)
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function updateConfiguration(configuration) {
	let data = null;
	try {
		data = await updateConfigurationModel(configuration)
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function startTrainingModel(model) {
	let data = null;
	try {
		data = await startTrainingIteration(model)
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function callEnablers() {
	let data = null;
	try {
		data = await recoverStatusFromEnablers()
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function loadModelData() {
	let data = null;
	try {
		data = await insertAditionalModelData()
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}

async function modelData() {
	let data = null;
	try {
		data = await recoverModelData()
	} catch (error) {
		throw new CustomError(error.response.data, error.response.status);
	}
	return data;
}
