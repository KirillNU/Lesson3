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

for i in range(2):
    input_sequence = input(f'Введите {i+1}-ю последовательность цифр, разделенные символами", ; : /" \n')
    formatted_sequence = input_sequence.replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('/', ' ').split()
    unique_set = set(formatted_sequence)
print(input_sequence, type(input_sequence))
#final_list = str(unique_set).replace('{', '').replace('}', '').replace('\'', '')
#print(final_list)

