# Build the application for production
FROM node:14.15.4-alpine AS builder

# instalar dependencias del proyecto
RUN apk add --no-cache git
RUN apk add --no-cache python
RUN npm install -g node-gyp
RUN apk add --virtual build-dependencies build-base gcc wget git
RUN git config --global url."https://".insteadOf git://

WORKDIR /app

COPY . .
RUN npm install
RUN npm rebuild node-sass
COPY ./update/v-shell.vue ./node_modules/vue-shell/src/v-shell.vue
RUN npm run build:prod

# Build an nginx-based image
FROM nginx:1.22.0-alpine

WORKDIR /usr/share/nginx/html

# RUN rm -rf ./*
# RUN mkdir -p /usr/share/nginx/html/
COPY --from=builder /app/dist ./

COPY ./docker/nginx/templates /etc/nginx/templates
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV FL_GUI_UI_HOST_PORT =  8080
ENV FL_GUI_API_HOST_NAME =  localhost
ENV FL_GUI_API_PORT =  3000
ENV FL_GUI_API_WS_PORT =  3010



ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
