# Deploying FL Orchestrator GUI Helm chart

1. Create a Secret to access Assist-iot's private container registry
```bash
kubectl create secret docker-registry regcred --docker-server=https://gitlab.assist-iot.eu:5050/ --docker-username=<your-name> --docker-password=<your-pword/token> --docker-email=<your-email>
```
2. Deploy dependencies
  - FL-Localoperations: https://gitlab.assist-iot.eu/wp5/t52/fl-local-operations
  - FL-Training Collector KPI enabler: https://gitlab.assist-iot.eu/wp5/t52/fl-training-collector
  - FL-Respository KPI enabler: https://gitlab.assist-iot.eu/wp5/t52/fl-repository

3. Deploy helm chart
```bash
helm install fl-orchestrator-gui ./helm-chart/
```

Other commands

```bash
# Get all release
helm list

#Delete release
helm uninstall <name-release>

```