import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import logger from './config/winston';
import config from './config/config';
import util from './middlewares/util';
import auth from './middlewares/auth';

import repository from './controllers/repository.controller';
import orchestrator from './controllers/orchestrator.controller';
import notification from './controllers/notification.controller';


const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(util.languageParser);
app.use(cors());

// Routes
app.use('/repository', auth.authUser, auth.isAuthorized, repository);
app.use('/orchestrator', auth.authUser, auth.isAuthorized, orchestrator);
app.use('/notification', auth.authUser, auth.isAuthorized, notification);

// app.listen(config.PORT, () => logger.info(`Listen on ${config.PORT} port`));
const server = app.listen(config.PORT, () => logger.info(`Listen on ${config.PORT} port`));
