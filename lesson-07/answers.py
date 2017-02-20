# Задача 1
#
# сделать генератор, который бесконечно по кругу возвращает последовательность
# чисел сначала от 1 до 10 по возрастанию, потом от 10 до 1 по убыванию:
# 1, 2, 3 ... 10, 9, 8 ... 1, 2, 3, ... 10 ... 1 ... 10 ...

import itertools

# generator = itertools.chain.from_iterable(
#     itertools.repeat(
#         itertools.chain(
#             range(1, 10),
#             range(10, 1, -1)
#         )
#     )
# )
# for i, v in enumerate(generator):  # не работает
#     if i < 300:
#         print(i, v)
#     else:
#         break

generator = itertools.chain.from_iterable(
    (
        x() for x in itertools.repeat(
            lambda: itertools.chain(
                range(1, 10),
                range(10, 1, -1)
            )
        )
    )
)
for i, v in enumerate(generator):  # работает
    if i < 30:
        print(i, v)
    else:
        break


# Задача 2
#
# Посчитать сколько раз на странице https://www.python.org/ встречается слово «python».

import requests

r = requests.get('http://www.python.org/')
if r.status_code == 200:
    word = 'python'
    content = r.content.decode()
    cnt = (len(content)-len(content.lower().replace(word, ''))) // len(word)
    print("Слово '{}' встречается {} раз".format(word, cnt))
else:
    print("не удалось скачать страницу")


# Задача 3
#
# Решите задачу используя defaultdict
# Прочитайте из файла ключевые слова (по одному в строке) и выведите
# на экран те из них, которые встречаются более одного раза, в порядке
# уменьшения частоты вхождений в исходный файл. Следует игнорировать
# регистр букв (прописные/заглавные).
#
# Пример на входе:
# 	microsoft
# 	apple
# 	Microsoft
# 	Apple
# 	security
# 	Microsoft
# 	Internet
# Пример на выходе:
# 	microsoft: 3
# 	apple: 2

from collections import defaultdict

words = defaultdict(lambda: 0)
with open('../lesson-4/source.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words[line.strip().lower()] += 1

for word, cnt in sorted(words.items(), key=lambda x: x[1], reverse=True):
    if cnt > 1:
        print("{}: {}".format(word, cnt))


# Задача 4
# Сохранить список всех ссылок со страницы https://www.python.org/
# в CSV файл в формате:  «URL», «текст ссылки»

import requests
import re

source_url = 'http://www.python.org/'
r = requests.get(source_url)
if r.status_code == 200:
    content = r.content.decode()

    for match in re.finditer(r"""<a[^>]*href=['"](.*?)['"][^>]*>(.*?)</a>""", content):
        url, title = match.group(1, 2)
        if url.startswith('/'):
            url = source_url[:-1] + url  # нужно удалить завершающий символ '/'
        print("{}\t{}".format(url, title))

else:
    print("не удалось скачать страницу")
