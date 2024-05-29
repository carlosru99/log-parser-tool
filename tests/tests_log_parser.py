import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main_data_parser import parse_log, str_to_datetime

def test_parse_log_with_valid_range_and_host():
    time_init = str_to_datetime("2019-08-12 00:00:00")
    time_end = str_to_datetime("2019-08-13 23:59:59")
    hostname = 'Keimy'
    
    expected_connections = ['Dmetri', 'Sarann']
    connections = parse_log("log.txt", time_init, time_end, hostname)
    
    assert connections == expected_connections


def test_parse_log_with_valid_range_and_host_2():
    time_init = str_to_datetime("2019-02-21 14:34:24")
    time_end = str_to_datetime("2019-08-13 06:05:24")
    hostname = 'Zaiden'
    
    expected_connections = ['Aralis']
    connections = parse_log("log.txt", time_init, time_end, hostname)
    
    assert connections == expected_connections

def test_parse_log_with_no_connections():
    time_init = str_to_datetime('2019-08-12 00:00:00')
    time_end = str_to_datetime('2019-08-14 23:59:59')
    hostname = 'NoHost'
    
    expected_connections = []
    connections = parse_log("log.txt", time_init, time_end, hostname)
    
    assert connections == expected_connections

def test_parse_log_with_short_time_range():
    time_init = str_to_datetime('2020-08-12 00:00:00')
    time_end = str_to_datetime('2020-08-12 00:01:00')
    hostname = 'Keimy'
    
    expected_connections = []
    connections = parse_log("log.txt", time_init, time_end, hostname)
    
    assert connections == expected_connections

