from prometheus_client import make_asgi_app
from prometheus_client.core import REGISTRY
from prometheus_client import Counter, Histogram
from fastapi import FastAPI
import psutil

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

def setup_metrics(app: FastAPI):
    metrics_app = make_asgi_app()
    app.mount("/metrics", metrics_app)
    REGISTRY.register(ProcessCollector())

class ProcessCollector:
    def collect(self):
        process = psutil.Process()
        yield GaugeMetricFamily(
            'process_memory_rss',
            'Resident memory used',
            value=process.memory_info().rss
        )
        yield GaugeMetricFamily(
            'process_cpu_percent',
            'CPU percent',
            value=process.cpu_percent()
        )