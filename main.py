import datetime

def parse_log(
            file_path: str,
            time_init: datetime.datetime,
            time_end: datetime.datetime,
            hostname: str) -> list:
    """
    Parses a log file to find connections between hosts in a specified time range.

    Args:
        file_path (str): The path to the log file.
        time_init (datetime): The start time of the time range.
        time_end (datetime): The end time of the time range.
        hostname (str): The hostname to find connections for.

    Returns:
        list: A list of hostnames connected to the target_hostname within the specified time range.
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

