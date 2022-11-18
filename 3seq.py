# МОДУЛЬ 3 3seq.py
'''
Задание:

- Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
- Затем он вводит элементы 2-го списка
- Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
'''

#input_sequence = '1,2;3:4,5,6/6,7,9,45,31,5,31' - для тестирования
list_of_unique_sets = []
for i in range(2):
    input_sequence = input(f'Введите {i+1}-ю последовательность цифр, разделенные символами", ; : /" \n')
    formatted_sequence = input_sequence.replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('/', ' ').split()
    list_of_unique_sets.append(set(formatted_sequence))

x = list_of_unique_sets[0]
y = list_of_unique_sets[1]
x.difference_update(y)

final_list = str(x).replace('{', '').replace('}', '').replace('\'', '')
print(final_list)

