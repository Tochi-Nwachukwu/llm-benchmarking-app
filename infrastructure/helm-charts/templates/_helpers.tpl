{{/*
Generate a fullname for the chart by concatenating the release name and the chart name.
*/}}
{{- define "llm-benchmark.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride }}
{{- else }}
{{- .Release.Name }}-{{ .Chart.Name }}
{{- end }}
{{- end }}

{{/*
Generate a name for the chart.
*/}}
{{- define "llm-benchmark.name" -}}
{{- .Chart.Name }}
{{- end }}