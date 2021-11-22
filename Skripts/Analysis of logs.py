import apache_log_parser
import csv

line_parser = apache_log_parser.make_parser("%v %h %l %u %t \"%r\" %>s %b")

csv_file = open('log.csv', 'w')
data = [['remote_host', 'server_name2', 'query_string', 'time_received_isoformat', 'request_method', 'request_url', 'request_http_ver', 'request_url_scheme', 'request_url_query', 'status', 'response_bytes_clf', 'request_header_user_agent', 'request_header_user_agent_browser_family', 'request_header_user_agent_browser_version_string', 'request_header_user_os_family', 'request_header_user_agent_os_version_string', 'request_header_user_agent_is_mobile']]
with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
csv_file.close()

with open('all_log.log') as file:
    for line in file:
        line = line.strip()
        line_parser = apache_log_parser.make_parser("%h %V %q %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
        log_line_data = line_parser(f'{line}')
        data = [[log_line_data['remote_host'], log_line_data['server_name2'], log_line_data['query_string'],
                 log_line_data['time_received_isoformat'], log_line_data['request_method'],
                 log_line_data['request_url'], log_line_data['request_http_ver'], log_line_data['request_url_scheme'],
                 log_line_data['request_url_query'], log_line_data['status'], log_line_data['response_bytes_clf'],
                 log_line_data['request_header_user_agent'],
                 log_line_data['request_header_user_agent__browser__family'],
                 log_line_data['request_header_user_agent__browser__version_string'],
                 log_line_data['request_header_user_agent__os__family'],
                 log_line_data['request_header_user_agent__os__version_string'],
                 log_line_data['request_header_user_agent__is_mobile']]]
        csv_file = open('log.csv', 'a')
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
print('end')

import pandas as pd

data = pd.read_csv('log.csv')

status_code_count = data['status'].value_counts()
print(status_code_count)

data[data['status'] == 410]['request_header_user_agent__browser__family'].value_counts()
data_YandexBot = data[data['request_header_user_agent__browser__family']=='YandexBot']