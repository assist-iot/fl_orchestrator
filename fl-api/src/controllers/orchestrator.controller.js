import express from 'express';
import logger from '../config/winston';
import orchestratorService from '../services/orchestrator.service';

import CustomError from '../utils/CustomError';
import variables from '../utils/variables';

const router = express.Router();

// routes
router.post('/modelConfiguration', modelConfiguration);
router.get('/configurationByModel/:id', configurationModel);
router.post('/updateConfiguration', updateConfiguration);
router.post('/startTrainingModel', startTrainingModel);
router.get('/callEnablers', callEnablers);
router.get('/loadModelData',loadModelData);
router.get('/modelData',modelData);
router.post('/showConfiguration',showConfiguration);
router.get('/persistConfiguration',persistConfiguration);
router.post('/trainedConfiguration',trainedConfiguration);
export default router;

// Implementation
async function modelConfiguration(req, res) {
	const configuration = req.body;
	try {
		const data = await orchestratorService.modelConfiguration(configuration);
	res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			error: {
				status: 'Error',
				message: 'An error occurred'
			}
		});
	}
	return null;
}
async function trainedConfiguration(req, res) {
	const configurationId = req.body;
	try {
		const data = await orchestratorService.trainedConfiguration(configurationId);
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			error: {
				status: 'Error',
				message: 'An error occurred'
			}
		});
	}
	return null;
}
async function persistConfiguration(req, res) {
	try {
		const data = await orchestratorService.persistConfig();
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			error: {
				status: 'Error',
				message: 'An error occurred'
			}
		});
	}
	return null;
}		
async function showConfiguration(req, res) {
	const configuration = req.body;
	try {
		const data = await orchestratorService.showConfiguration(configuration);
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			error: {
				status: 'Error',
				message: 'An error occurred'
			}
		});
	}
	return null;
}	
async function configurationModel(req, res) {
	const { params: { id } = { id: null } } = req;
	try {
		const data = await orchestratorService.configurationModel(id);

		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			status: 'Error',
			message: 'An error occurred'
		});
	}
	return null;
}

async function updateConfiguration(req, res) {
	const configuration = req.body;
	try {
		const data = await orchestratorService.updateConfiguration(configuration);
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			error: {
				status: 'Error',
				message: 'An error occurred'
			}
		});
	}
	return null;
}

async function startTrainingModel(req, res) {
	const model = req.body;
	try {
		const data = await orchestratorService.startTrainingModel(model);
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			error: {
				status: 'Error',
				message: 'An error occurred'
			}
		});
	}
	return null;
}

async function callEnablers(req, res) {
	const { params: { id } = { id: null } } = req;

	try {
		const data = await orchestratorService.callEnablers();
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			status: 'Error',
			message: 'An error occurred'
		});
	}
	return null;
}

async function loadModelData(req, res) {
	try {
		const data = await orchestratorService.loadModelData();
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			status: 'Error',
			message: 'An error occurred'
		});
	}
	return null;
}

async function modelData(req, res) {
	try {
		const data = await orchestratorService.modelData();
		res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: data
		});
	} catch (error) {
		logger.error(error);
		if (error instanceof CustomError) {
			// eslint-disable-next-line
			const { message, name, stack, type } = error;
			return res.status(type).json({
				status: name,
				message: message.message
			});
		}
		return res.status(variables.NOT_FOUND).json({
			status: 'Error',
			message: 'An error occurred'
		});
	}
	return null;
}