from datetime import datetime, timedelta
import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def append_logs(initial_datetime, interval_seconds, num_records, host_from, host_to):
    for _ in range(num_records):
        with open("log.txt", 'a') as f:
            current_datetime = initial_datetime
            timestamp_ms = int(current_datetime.timestamp() * 1000)
            time.sleep(2)
            f.write(f"{timestamp_ms} {host_from} {host_to}\n")
            current_datetime += timedelta(seconds=interval_seconds)
    print(f"Appended {num_records} logs to log.txt")

initial_datetime = datetime.now()
interval = 10
num_records = 100
host_from = "hostX"
host_to = "hostZ"
log_file = "log.txt"

append_logs(initial_datetime, interval, num_records, host_from, host_to)
