# Задача 5. Вариант 1.
# Напиши программу,которая бы при запуске случайным образом
# отображала название одного из семи чудес света.
# Ажигов А.М.
#01.04.2017

import random
names = ('Пирамида Хеопса', 'Висячие сады Семирамиды', 'Статуя Зевса в олимпии', 'Храм Артемиды в Эфесе', 'Мавзолей в Галикарнасе', 'Колосс Родосский', 'Александрийский маяк')
print ("Один из семи чудес света ---  \n\n" + random.choice(names))
input ('\n\nНажмите Enter, чтобы продолжить') 
