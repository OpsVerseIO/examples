# Auto-Instrument Your App Using the OpenTelemetry Operator

A hands-on, 30-minute session on steps to auto instrument your apps running on Kubernetes to send distributed traces

## Steps

### Prerequisites

- A Kubernetes cluster (k3s, kind, microk8s, gke/
- An App (see the `deploy/` directory)
- A tracing backend (e.g., Jaeger; you can [launch one here](https://opsverse.io/observenow-observability/))

### Steps

Goal: your app will send traces to the collector, which in turn exports to your tracing backend. How do we get the app to automatically send traces?

1. Install the [OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator) onto your K8s cluster (configure the OpenTelemetry Collector to send to your traces backend)
2. Deploy the app annotated app
3. Interact with the app and view traces and insights
