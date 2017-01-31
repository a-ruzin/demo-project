# Задача 1
#
# Напишите декоратор, который кэширует результат вызова функции и возвращает его,
# если последующие вызовы этой функции производятся с теми же значениями
# параметров в течение 5 минут, но не более 10 раз

from datetime import datetime, timedelta
from time import sleep


def cache(func):
    cache_dict = {}
    def dec(*args, **kwargs):
        key = tuple(args) + tuple(((k, v) for k, v in sorted(kwargs.items(), key=lambda x: x[0])))
        if key in cache_dict and cache_dict[key][0] < 10 and datetime.now()-cache_dict[key][1] < timedelta(seconds=5):
            cache_dict[key][0] += 1
        else:
            cache_dict[key] = [1, datetime.now(), func(*args, **kwargs)]
        return cache_dict[key][2]
    return dec


@cache
def f1(a):
    print('f1 is called with {}'.format(a))
    return a + 10

for x in range(20):
    print(f1(x))

print('-'*100)

for x in range(20):
    print(f1(1))

print('-'*100)

for x in range(20):
    sleep(1)
    print(f1(1))

# Задача 2
#
# Прочитайте из файла ключевые слова (по одному в строке) и выведите на экран те из них,
# которые встречаются более одного раза, в порядке уменьшения частоты вхождений в исходный файл.
# Следует игнорировать регистр букв (прописные/заглавные).
# Пример на входе:
#          microsoft
#          apple
#          Microsoft
#          Apple
#          security
#          Microsoft
#          Internet
#  Пример на выходе:
#       microsoft: 3
#       apple: 2

words = {}
with open('source.txt', 'r') as f:
    for line in f:
        word = line.strip().lower()
        if word:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

for word in sorted(words.items(), key=lambda x: x[1], reverse=True):
    if word[1] > 1:
        print("{}: {}".format(*word))
