# FL-GUI API
## Quick Start

Install dependencies:

```bash
$ npm install
```

Start the server:
```bash
$ npm serve
```

Copy v-shell
In order to properly work the UI, the v-shell file of the folder "orchestrator-UI/node_modules/vue-shell/src" should be replaced by the one provided in the "update" folder of the project:

```
cp ./update/v-shell.vue ./node_modules/vue-shell/src/v-shell.vue
```

View the api at:
http://localhost:3000


## Assist-Iot WP5 T52 FL GUI Container Registry

Build image

```bash
docker build -t gitlab.assist-iot.eu:5050/wp5/t52/fl-gui/fl-gui.api:latest -f ./Dockerfile .
```

Push image to Container Registry

```
docker push gitlab.assist-iot.eu:5050/wp5/t52/fl-gui/fl-gui.api:latest
```