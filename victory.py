#МОДУЛЬ 4 victory.py
'''
Задание
Написать или улучшить программу Викторина из предыдущего дз
(Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy')
- предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample

Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ,
но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''

# Джек Лондон - 22.11.1876
# Бернард Шо - 26.07.1856
# Илья Ильф - 15.10.1897
# Евгений Петров - 13.12.1902
# Михаил Жванецкий - 06.03.1934
# Василий Аксёнов - 20.08.1932
# Ромен Роллан - 29.01.1866
# Михаил Булгаков - 15.05.1891
# Аркадий Стругацкий - 28.07.1925
# Борис Стругацкий - 15.04.1933

import random

lond = {'by': '1876', 'day_dig': '22', 'day_word': 'двадцать второе',
        'month_dig': '11', 'month_word': 'ноября',
        'name_genitive': 'Дж. Лондона'}

shaw = {'by': '1856', 'day_dig': '26', 'day_word': 'двадцать шестое',
        'month_dig': '07', 'month_word': 'июля',
        'name_genitive': 'Б. Шо'}

ilf = {'by': '1897', 'day_dig': '15', 'day_word': 'пятнадцатое',
       'month_dig': '10', 'month_word': 'октября',
       'name_genitive': 'И. Ильфа'}

petr = {'by': '1902', 'day_dig': '13', 'day_word': 'тринадцатое',
        'month_dig': '12', 'month_word': 'декабря',
        'name_genitive': 'Е. Петрова'}

jvan = {'by': '1934', 'day_dig': '06', 'day_word': 'шестое',
        'month_dig': '03', 'month_word': 'марта',
        'name_genitive': 'М. Жванецкого'}

aks = {'by': '1932', 'day_dig': '20', 'day_word': 'двадцатое',
       'month_dig': '08', 'month_word': 'августа',
       'name_genitive': 'В. Аксёнова'}

rol = {'by': '1866', 'day_dig': '29', 'day_word': 'двадцать девятое',
       'month_dig': '01', 'month_word': 'января',
       'name_genitive': 'Р. Роллана'}

bul = {'by': '1891', 'day_dig': '15', 'day_word': 'пятнадцатое',
       'month_dig': '05', 'month_word': 'мая',
       'name_genitive': 'М. Булгакова'}

astr = {'by': '1925', 'day_dig': '28', 'day_word': 'двадцать восьмое',
        'month_dig': '07', 'month_word': 'июля',
        'name_genitive': 'А. Стругацкого'}

bstr = {'by': '1933', 'day_dig': '15', 'day_word': 'пятнадцатое',
        'month_dig': '04', 'month_word': 'апреля',
        'name_genitive': 'Б. Стругацкого'}

writers_list = (lond, shaw, ilf, petr, jvan, aks, rol, bul, astr, bstr)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

max_good = 0
max_bad = 0
max_total = 0
cycle_total = 0

while True:
    ans_good = 0
    ans_bad = 0
    ans_total = 0

    writers = random.sample(numbers, 5)

    for selected in writers:
        w_name = writers_list[selected-1].get('name_genitive')
        d_dig = writers_list[selected-1].get('day_dig')
        d_word = writers_list[selected-1].get('day_word')
        m_dig = writers_list[selected-1].get('month_dig')
        m_word = writers_list[selected - 1].get('month_word')
        b_ye = writers_list[selected-1].get('by')

        inp_date = input(f'Введите дату рождения {w_name} в формате ДД.ММ.ГГГГ > ')

        if inp_date == f'{d_dig}.{m_dig}.{b_ye}':
            ans_good += 1
            ans_total += 1
        else:
            ans_bad += 1
            ans_total += 1
            print(f'Неверно. День рождения {w_name} {d_word} {m_word} {b_ye} года')

    print('За один цикл игры \n',
          'Количество Правильных ответов:', ans_good, '\n',
          'Количество Неправильных ответов:', ans_bad, '\n',
          'Процент Правильных ответов:', (ans_good / ans_total) * 100, '% \n',
          'Процент Неправильных ответов:', (ans_bad / ans_total) * 100, '% \n'
          )

    max_good = max_good + ans_good
    max_bad = max_bad + ans_bad
    max_total = max_total + ans_total
    cycle_total += 1

    more_attmpt = input('Попробуем еще раз? Да/Нет \n')

    if more_attmpt != 'Да':
        print('За все циклы', cycle_total, '\n',
          'Общее Количество Правильных ответов:', max_good, '\n',
          'Общее Количество Неправильных ответов:', max_bad, '\n',
          'Общий Процент Правильных ответов:', (max_good / max_total) * 100, '% \n',
          'Общий Процент Неправильных ответов:', (max_bad / max_total) * 100, '% \n'
              )
        break

print('Закончили')