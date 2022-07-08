words = ['инженер-конструктор Игорь',
         'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАй',
         'директор аэлита']
print(id(words))

indx = 1

print('List of available users')
for i in range(len(words)):
    words[i] = words[i].split(' ')
    words[i][-1] = words[i][-1].capitalize()
    user = words[i][-1]
    print((indx, user))
    indx += 1

user = int(input('Select your user number '))
print('Hello,', words[user-1][-1], '!')
print(id(words))
