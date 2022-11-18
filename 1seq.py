# МОДУЛЬ 1seq.py
'''
Создать новый проект, в нем создать модуль 1seq.py.
Задание:
- Пользователь вводит количество элементов будущего списка
- После этого по очереди по одной вводит любые цифры
- Сохранить цифры в список
- Отсортировать список по возрастанию и вывести на экран
- Пример работы: Введите количество элементов: 3
- Введите 1 элемент: 5
- Введите 2 элемент: 2
- Введите 3 элемент: 4
- Вывод: [2, 4, 5]
'''
while True:
    list_size = input('Введите число элементов списка: \n')
    if not list_size.isdigit():
        print('Вы ввели не число')
    else:
        cycle_count = int(list_size)
        break

list_elements = []

for i in range(cycle_count):
    try:
        x = int(input(f'Введите {i+1}  элемент: '))
        list_elements.append(x)
    except:
        print(f'Введённый Элемент {i+1} не число')

print(sorted(list_elements))
# print(list_elements.sort()) - не работает. Вопрос куратору - почему?
