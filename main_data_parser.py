import datetime
import sys

def parse_log(
            file_path: str,
            time_init: datetime.datetime,
            time_end: datetime.datetime,
            hostname: str) -> list:
    """
    Parses a log file to find connections between hosts in a specified time range

    Args:
        file_path (str): The path to the log file
        time_init (datetime): The start time of the time range
        time_end (datetime): The end time of the time range
        hostname (str): The hostname to find connections for

    Returns:
        list: A list of hostnames connected to the target within the specified time range
    """

    connections = []
    time_init_ts = int(time_init.timestamp() * 1000)
    time_end_ts = int(time_end.timestamp() * 1000)

    with open(file_path, 'r', encoding='utf-8') as file:
        for log in file:
            splitted_file = log.strip().split(sep=" ")
            timestamp = int(splitted_file[0])
            if time_init_ts <= timestamp <= time_end_ts:
                host_from = splitted_file[1]
                host_to = splitted_file[2]
                if host_from == hostname:
                    connections.append(host_to)

    return connections


def str_to_datetime(date_str: str) -> datetime.datetime:
    
    """
    Convert stringified datetime in '%Y-%m-%d %H:%M:%S' format into datetime .

    Args:
        date_str (str): datetime in string format.

    Returns:
        datetime.datetime: A datetime.datetime format value
    """

    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

def main():
    if len(sys.argv) != 5:
        print("Correct input format: python main.py <nombre_archivo> <init_timestamp> <end_timestamp> <hostname>")
        sys.exit(1)

    try:
        file_path = sys.argv[1]
        time_init = str_to_datetime(sys.argv[2])
        time_end = str_to_datetime(sys.argv[3])
        hostname = sys.argv[4]

        connections = parse_log(file_path, time_init, time_end, hostname)
        print(f"Found connections for host \"{hostname}\":", connections)
    except ValueError as ve:
        print(f"Datetime input format: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpeceted error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()