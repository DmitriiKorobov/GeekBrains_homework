import re
import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = str(requests.get(URL).text)

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.writelines(response)

with open('parsed_nginx_logs.txt', 'w', encoding='utf-8') as f:
    file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')

    for line in file_1:
        try:
            data = [re.search(r'\d*\.\d*\.\d*\.\d*', line).group(0),
                    re.search(r'\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}', line).group(0),
                    re.search(r'(POST|GET|PUT|OPTION|HEAD)', line).group(0),
                    re.search(r'(/\w{9}/\w{9})', line).group(0),
                    re.search(r'\d{3}\s\d+', line).group(0).split(' ')[0],
                    re.search(r'\d{3}\s\d+', line).group(0).split(' ')[1]]
            f.writelines(str(data) + '\n')
        except AttributeError:
            continue