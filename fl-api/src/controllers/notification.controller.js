import express from 'express';
import logger from '../config/winston';

import CustomError from '../utils/CustomError';

import variables from '../utils/variables';

import wsSocket from '../utils/wsSocket';
const webSocket = new wsSocket(3010);

const router = express.Router();

// routes
router.post('/', uiNotification);
router.post('/errorNotification', errorNotification);


export default router;

// Implementation
async function uiNotification(req, res){
    const bodyMsg = req.body

    try {
        const { socket } = webSocket;

        const data = {
            'type': 'SUCCESS',
            'model_name': bodyMsg.model_name,
            'model_version': bodyMsg.model_version,
            'round': bodyMsg.round
        }
        const message = `${data.type},${data.model_name},${data.model_version},${data.round}`;
        
		socket.send(message);
        
        return res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: 'Message sended to UI'
		});

    } catch (error) {
        logger.error(error);
        if (error instanceof CustomError) {
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
    // return null;
}

async function errorNotification(req, res){
    const bodyMsg = req.body
    try {

        const { socket } = webSocket;

        const data = {
            'type': bodyMsg.type,
            'enabler': bodyMsg.id,
            'message': bodyMsg.message,
            'additionalInfo': bodyMsg.additionalInfo
        }
        const message = `${data.type},${data.enabler},${data.message},${data.additionalInfo}`;
		socket.send(message);
        
        return res.status(variables.CORRECT_REQUEST).json({
			status: 'OK',
			message: 'Message sended to UI'
		});

    } catch (error) {
        logger.error(error);
        if (error instanceof CustomError) {
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
    //return null;
}