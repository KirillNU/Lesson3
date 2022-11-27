#(МОДУЛЬ 2) 2seq.py
'''Cоздать модуль 2seq.py.
Задание:
- Пользователь вводит любые цифры через запятую
- Сохранить цифры в список
- Получить новый список в котором будут только уникальные элементы исходного
  (уникальным считается символ, который встречается в исходном списке только 1 раз)
- Вывести новый список на экран
- Порядок цифр в новом списке не важен
- Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
- Результат: 2, 4, 6, 9

(Дополнительно*) Предусмотреть что пользователь может использовать:
один из 3-х разделителей:
a. запятую,
b. точку с запятой,
c. слэш (1,2,3 1;2;3 1/2/3),
d. но только какой то один 1,2;3/4 - так нельзя
'''

input_sequence = '1,2;3:4,5,6/6,7,9,45,31,5,31'
# Добавлены символы разделителей и пункт d. изменен - допускается комбинация разделителей

#input_sequence = input('Введите последовательность цифр, разделенные символами", ; : /" \n')
formatted_sequence = input_sequence.replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('/', ' ').split()
unique_set = set(formatted_sequence)
final_list = str(unique_set).replace('{', '').replace('}', '').replace('\'', '')
print(final_list)

