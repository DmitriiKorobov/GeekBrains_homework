words = ['в', '5', 'часов', '17', 'минут', 'температура',
         'воздуха', 'была', '+5', 'градусов']
word_ind = []
print(id(words))

for i in range(len(words)):
    if words[i].isdigit():
        if len(words[i]) == 1:
            words[i] = str(0) + words[i]
            word_ind.append(i)
            word_ind.append(i + 1)
        else:
            word_ind.append(i)
            word_ind.append(i+1)
    else:
        d = range(len(words[i]))
        for f in d:
            if words[i][f].isdigit():
                words[i] = words[i][0] + str(0) + words[i][-1]
                word_ind.append(i)
                word_ind.append(i + 1)
word_ind.reverse()

for ind in word_ind:
    words.insert(ind, '"')

print(id(words))
print(' '.join(words))