import sys
import time
from datetime import datetime, timedelta

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def process_new_logs(log_file_path, from_hostname, to_hostname):
    connections_sent = []
    connections_received = []

    connections_count = {}

    initial_print_done = False

    with open(log_file_path, 'r', encoding='utf-8') as file:
        new_lines = follow(file)
        
        if not initial_print_done:
            file.seek(0, 0)
            for line in file:
                print(line.strip())
            initial_print_done = True
        starting_hour = datetime.now()
        target_hour = starting_hour + timedelta(hours=1)

        while True:
            for line in new_lines:

                splitted_file = line.strip().split()
                connection_timestamp, host_from, host_to = splitted_file
                connection_datetime = datetime.fromtimestamp(int(connection_timestamp) / 1000)

                if host_from == from_hostname:
                    connections_sent.append((connection_datetime, host_to))
                if host_to == to_hostname:
                    connections_received.append((connection_datetime, host_from))
                if host_from in connections_count:
                    connections_count[host_from] += 1
                else:
                    connections_count[host_from] = 1

                if datetime.now() >= target_hour:
                    connected_to = [host for ts, host in connections_received if ts > starting_hour - timedelta(hours=1)]
                    connected_from = [host for ts, host in connections_sent if ts > starting_hour - timedelta(hours=1)]

                    most_connections = max(connections_count.items(), key=lambda x: x[1], default=(None, 0))

                    print(f"Time: {datetime.now()}")
                    print(f"Connections to {to_hostname} in the last hour: {connected_to}")
                    print(f"Connections from {from_hostname} in the last hour: {connected_from}")
                    print(f"Hostname with most connections: {most_connections[0] if most_connections else None}")

                    # Actualizar tiempos y reiniciar contadores
                    starting_hour = target_hour
                    target_hour = target_hour + timedelta(hours=1)

                    connections_sent = []
                    connections_received = []
                    connections_count = {}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python realtime_log_parser.py <log_file_path> <from_hostname> <to_hostname>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    from_hostname = sys.argv[2]
    to_hostname = sys.argv[3]

    process_new_logs(log_file_path, from_hostname, to_hostname)
