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





# '''
# j_lond = '1876' #Джек Лондон
# b_shaw = '1856' #Бернард Шо
# i_ilf = '1897' #Илья Ильф
# e_petr = '1902' #Евгений Петров
# m_jvan = '1934' #Михаил Жванецкий
# v_akse = '1932' #Василий Аксёнов

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
writers = random.sample(numbers, 5)

print(writers, type(writers))


month_names = {'01': 'января', '02': 'февраля', '03': 'марта',
               '04': 'апреля', '05': 'мая', '06': 'июня',
               '07': 'июля', '08': 'августа', '09': 'сентября',
               '10': 'октября','11': 'ноября','12': 'декабря'
               }

day_names = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое', '06': 'шестое',
             '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одинадцатое',
             '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
             '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
             '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцатьпервое', '22': 'двадцатьвторое',
             '23': 'двадцатьтретье', '24': 'двадцатьчетвёртое', '25': 'двадцатьпятое', '26': 'двадцатьшестое',
             '27': 'двадцатьседьмое', '28': 'двадцатьвосьмое', '29': 'двадцатьдевятое',
             '30': 'тридцатое', '31': 'тридцатьпервое' }

writers_dict = {'уear': '', 'day_dig': '', 'day_word': '', 'month_dig': '', 'month_word': '', 'name_genitive': ''}

writers_list = []



# print(month_names)
# print(day_names)
# print(writers_dict)

# day_names =
#
# writer_dict = {'Year': '1921', "Day_d": , '08', 'Day_w': }