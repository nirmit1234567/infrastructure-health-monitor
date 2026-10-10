
from prometheus_client import start_http_server, Gauge
import psutil
import time

cpu_usage = Gauge("system_cpu_usage_percent", "CPU usage percentage")
memory_usage = Gauge("system_memory_usage_percent", "Memory usage percentage")
disk_usage = Gauge("system_disk_usage_percent", "Disk usage percentage")

def collect_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage("/").percent)

if __name__ == "__main__":
    start_http_server(8000)
    print("Metrics exporter running on port 8000")

    while True:
        collect_metrics()
        time.sleep(15)
