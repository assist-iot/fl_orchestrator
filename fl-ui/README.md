# FL-GUI UI
## Quick Start

Install dependencies:

```bash
$ npm install
```

Copy v-shell
In order to properly work the UI, the v-shell file of the folder "orchestrator-UI/node_modules/vue-shell/src" should be replaced by the one provided in the "update" folder of the project:

```bash
cp ./update/v-shell.vue ./node_modules/vue-shell/src/v-shell.vue
```

Start the server:

```bash
$ npm run dev
```

View the api at:
 http://localhost:8080


## Assist-Iot WP5 T52 FL GUI Container Registry

Build image

```bash
docker build -t gitlab.assist-iot.eu:5050/wp5/t52/fl-gui/fl-gui.ui:latest -f ./docker/Dockerfile .
```

Push image to Container Registry
```
docker push gitlab.assist-iot.eu:5050/wp5/t52/fl-gui/fl-gui.ui:latest