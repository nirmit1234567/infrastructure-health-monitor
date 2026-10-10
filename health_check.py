
import platform
import psutil
import logging
from datetime import datetime

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

checks = {
    "CPU": psutil.cpu_percent(interval=1),
    "Memory": psutil.virtual_memory().percent,
    "Disk": psutil.disk_usage("C:\\").percent
}

print("\n=== System Health Report ===")
print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("OS:", platform.system())

for name, value in checks.items():
    status = "WARNING" if value >= 80 else "OK"
    message = f"{name} Usage: {value}% - {status}"

    print(message)
    logging.info(message)

print("Log saved to health_check.log")
