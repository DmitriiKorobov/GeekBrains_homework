import itertools

with open('users.csv', 'r', encoding='utf-8') as users:
    name_lst = [name[:-1].replace(',', ' ') for name in users]

with open('hobby.csv', 'r', encoding='utf-8') as hobbys:
    hobby_lst = hobbys.readline().replace(' ', '').split(',')

with open('data.csv', 'w', encoding='utf-8') as data:
    data_dic = str(dict(itertools.zip_longest(name_lst, hobby_lst)))
    data.write(data_dic)

    i = 0
    while i < len(name_lst) and i < len(hobby_lst):
        data.write(f'{name_lst[i]}: {hobby_lst[i]}')
        i += 1
    while i < len(name_lst) > len(hobby_lst) :
        data.write(f'{name_lst[i]}: {None}')
        i += 1
