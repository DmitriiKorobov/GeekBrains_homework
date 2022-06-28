file = open(r'/Volumes/Macintosh HD/Homework (GeekBrains)/Python Basics/'
            r'Lesson 6/Task 1/nginx_logs.txt', 'r', encoding='utf-8')


def attack(file):
    with open('ip.txt', 'w+', encoding='utf-8') as f:
        for line in file:
            f.writelines(f'{line.split(" ")[0]}\n')

    file_ip = open(r'/Volumes/Macintosh HD/Homework (GeekBrains)/Python Basics'
                   r'/Lesson 6/Task 2/ip.txt', 'r', encoding='utf-8')

    ip_lst = [line.strip() for line in file_ip]

    max_quan = 1
    spammer_ip = None
    for ip in ip_lst:
        req_quan = ip_lst.count(ip)
        if req_quan > max_quan:
            max_quan = req_quan
            spammer_ip = ip

    return spammer_ip, max_quan


print(f'Spammer ip: {attack(file)} request')
