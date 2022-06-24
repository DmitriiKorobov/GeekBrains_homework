import requests

response = str(requests.get('https://github.com/elastic/examples/raw/master'
                            '/Common%20Data%20Formats/nginx_logs/nginx_logs').text)

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(response)
file = open('nginx_logs.txt', 'r', encoding='utf-8')


def get_info(file):
    result = []
    for _ in file:
        line = file.readline().split(' ')
        result.append((line[0], line[5].replace('"', ''), line[6]))
    file.close()
    return result


with open('parsed_nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(str(get_info(file)))
