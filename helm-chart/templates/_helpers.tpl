{{/*
Expand the name of the chart.
*/}}
{{- define "enabler.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "enabler.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "enabler.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Cilium Multi-cluster global service annotations.
*/}}
{{- define "globalServiceAnnotations" -}}
io.cilium/global-service: "true"
io.cilium/service-affinity: remote
{{- end }}

{{/*
Name of the component orchestrator.
*/}}
{{- define "orchestrator.name" -}}
{{- printf "%s-orchestrator" (include "enabler.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified component orchestrator name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "orchestrator.fullname" -}}
{{- printf "%s-orchestrator" (include "enabler.fullname" .) | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Component orchestrator labels.
*/}}
{{- define "orchestrator.labels" -}}
helm.sh/chart: {{ include "enabler.chart" . }}
{{ include "orchestrator.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Component orchestrator selector labels.
*/}}
{{- define "orchestrator.selectorLabels" -}}
app.kubernetes.io/name: {{ include "enabler.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
enabler: {{ .Chart.Name }}
app.kubernetes.io/component: orchestrator
isMainInterface: "yes"
tier: {{ .Values.orchestrator.tier }}
{{- end }}

{{/*
Name of the component dbmongo.
*/}}
{{- define "dbmongo.name" -}}
{{- printf "%s-dbmongo" (include "enabler.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified component dbmongo name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "dbmongo.fullname" -}}
{{- printf "%s-dbmongo" (include "enabler.fullname" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create the default FQDN for dbmongo headless service.
*/}}
{{- define "dbmongo.svc.headless" -}}
{{- printf "%s-headless" (include "dbmongo.fullname" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Component dbmongo labels.
*/}}
{{- define "dbmongo.labels" -}}
helm.sh/chart: {{ include "enabler.chart" . }}
{{ include "dbmongo.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Component dbmongo selector labels.
*/}}
{{- define "dbmongo.selectorLabels" -}}
app.kubernetes.io/name: {{ include "enabler.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
enabler: {{ .Chart.Name }}
app.kubernetes.io/component: dbmongo
isMainInterface: "no"
tier: {{ .Values.dbmongo.tier }}
{{- end }}

{{/*
Name of the component api.
*/}}
{{- define "api.name" -}}
{{- printf "%s-api" (include "enabler.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified component api name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "api.fullname" -}}
{{- printf "%s-api" (include "enabler.fullname" .) | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Component api labels.
*/}}
{{- define "api.labels" -}}
helm.sh/chart: {{ include "enabler.chart" . }}
{{ include "api.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Component api selector labels.
*/}}
{{- define "api.selectorLabels" -}}
app.kubernetes.io/name: {{ include "enabler.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
enabler: {{ .Chart.Name }}
app.kubernetes.io/component: api
isMainInterface: "yes"
tier: {{ .Values.api.tier }}
{{- end }}

{{/*
Name of the component webapp.
*/}}
{{- define "webapp.name" -}}
{{- printf "%s-webapp" (include "enabler.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified component webapp name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "webapp.fullname" -}}
{{- printf "%s-webapp" (include "enabler.fullname" .) | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Component webapp labels.
*/}}
{{- define "webapp.labels" -}}
helm.sh/chart: {{ include "enabler.chart" . }}
{{ include "webapp.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Component webapp selector labels.
*/}}
{{- define "webapp.selectorLabels" -}}
app.kubernetes.io/name: {{ include "enabler.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
enabler: {{ .Chart.Name }}
app.kubernetes.io/component: webapp
isMainInterface: "no"
tier: {{ .Values.webapp.tier }}
{{- end }}

