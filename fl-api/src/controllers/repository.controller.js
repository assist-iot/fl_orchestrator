import express from 'express';
import logger from '../config/winston';
import repositoryService from '../services/repository.service';

import CustomError from '../utils/CustomError';
import variables from '../utils/variables';

const router = express.Router();

// routes
router.get('/getModels', getModels);
router.get('/availableModels/', availableModels);
router.post('/downloadModel', downloadModel);
router.get('/shell/model/:id/:version/:configid',getShellModel)
router.get('/getStrategy',getStrategies);
router.get('/training-results',trainingResults);

export default router;

// Implementation
async function getModels(req, res) {
	try {
		const data = await repositoryService.getModels();
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

async function availableModels(req, res) {
	try {
		const data = await repositoryService.availableModels();

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

async function downloadModel(req, res) {
	const model = req.body;
	try {
		const data = await repositoryService.downloadModel(model);
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

async function getShellModel(req, res) {
	const { params: { id,version,configid } = { id: null,version:null,configid:null } } = req;
	try {
		const data = await repositoryService.getShellModel(id,version,configid);
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

async function getStrategies(req, res) {
	try {
		const data = await repositoryService.getStrategies();
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

async function trainingResults(req, res) {
	try {
		const data = await repositoryService.trainingResults();
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
