from datetime import datetime, timedelta
import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

def append_logs(initial_datetime, interval_seconds, num_records, host_from, host_to):
    """
    Function developed to add registries into log.txt file for unlimited parser testing
    """
    current_datetime = initial_datetime
    for _ in range(num_records):
        with open("log.txt", 'a', encoding='utf-8') as f:
            timestamp_ms = int(current_datetime.timestamp() * 1000)
            time.sleep(2)
            f.write(f"{timestamp_ms} {host_from} {host_to}\n")
            current_datetime += timedelta(seconds=interval_seconds)
    print(f"Appended {num_records} logs to log.txt")

if __name__ == "__main__":
    initial_datetime = datetime.now()
    interval = 2
    num_records = 100
    host_from = "hostX"
    host_to = "hostZ"
    log_file = "log.txt"

    append_logs(initial_datetime, interval, num_records, host_from, host_to)
