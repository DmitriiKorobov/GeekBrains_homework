def generate(tutor, klass):
    i = 0
    while i < len(tutor) and i < len(klass):
        yield tutor[i], klass[i]
        i += 1
    while i < len(tutor):
        yield tutor[i], None
        i += 1


tutor = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Иван', 'Данила']
klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

for i in generate(tutor, klass):
    print(i, type(i))

answer = generate(tutor, klass)
