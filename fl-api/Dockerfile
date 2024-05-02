FROM node:14-slim
WORKDIR /api

ADD . /api

RUN npm install && npm run build

ENV NODE_ENV production

CMD ["npm", "run", "start"]