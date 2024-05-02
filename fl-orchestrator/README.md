## Docker
Build image

```bash
docker build -t fl-orchestrator-app:latest 
```

## Assist-Iot WP5 T52 Fl Orchestrator 

Build image

```bash
docker build -t gitlab.assist-iot.eu:5050/wp5/t52/fl-orchestrator/fl.orchestrator.app:latest -f ./Dockerfile .

Push image to Container Registry

```
docker push gitlab.assist-iot.eu:5050/wp5/t52/fl-orchestrator/fl.orchestrator.app:latest
```