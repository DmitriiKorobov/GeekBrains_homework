"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

!!!!!!!!!!!!!!!!!!!!!!!!!

Условие задачи я совершенно не понял.
1. В условии список, а в примере словарь
2. Почему первый элемент 4, а все остальные +3
3. Что именно нужно прогнать через последовательность (само n или же данные в словаре)

Поэтому я придумал свое условие:
1. К каждому элементу от 1 до n будет прибавлено +3
2. Все это выведится в словарь (не список)
3. Каждое значение словаря будет прогнано через формулу (1+1/n)**n
4. Полученное значение добавится в СПИСОК
5. Далее будет суммирование всех элементов списка и вывод ответа
"""

n = int(input('Enter number for n = '))


def s(n):
    create_dict = {}
    temp_for_dict = 1
    create_list = []
    temp_for_list = 0

    for i in range(1, n + 1):
        create_dict[i] = temp_for_dict + 3
        temp_for_dict = temp_for_dict + 3
    print(create_dict)

    for key in create_dict:
        create_list.append((1 + 1 / create_dict[key]) ** create_dict[key])
        temp_for_list = temp_for_list + (1 + 1 / create_dict[key]) ** create_dict[key]
    print(create_list)
    print('answer =', round(temp_for_list, 2))


s(n)
