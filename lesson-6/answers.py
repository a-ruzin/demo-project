# Задача 1
# Найти наименьшее число фибоначи, которое делится на заранее
# заданное число без остатка. При решении использовать генераторы

def fibbonachi():
    fibs = 0, 1
    while True:
        yield fibs[1]
        fibs = fibs[1], sum(fibs)

N = 1
for i, fib in enumerate(fibbonachi()):
    if i > 1000:
        print("too big number")
        break
    if fib % N == 0:
        print("found: {} at {}'th place".format(fib, i+1))
        break


# Задача 2
# Написать декоратор, который перехватывает любые исключения,
# производные от Exception, и записывает их в файл.
# При этом само исключение должно быть «переброшено» дальше.

def log(filename):
    def logger(func):
        def dec(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                with open(filename, 'a') as f:
                    print(str(e), file=f)
                raise
        return dec
    return logger

@log('exceptions.log')
def something_wrong(*args, **kwargs):
    raise Exception('something goes wrong with {} and {}'.format(args, kwargs))

# something_wrong(1, 2, key=34)


# Задача 3
# Написать аналог команды diff (построчное сравнение двух файлов).

def diff(filename1, filename2):
    with open(filename1, 'r') as f1, open(filename2, 'r') as f2:
        buf1 = []
        buf2 = []
        eof1 = False
        eof2 = False

        def readline(file, buf):
            line = file.readline()
            if line:
                buf.append(line)
            return line, line == ''

        def dumpbufs(b1, b2, i1, i2):
            for l in b1[:i1-1]:
                print("> {}".format(l), end="")
            for l in b2[:i2-1]:
                print("< {}".format(l), end="")
            return b1[i1:], b2[i2:]

        while True:
            line1, eof1 = readline(f1, buf1)
            line2, eof2 = readline(f2, buf2)
            if eof1 and eof2:
                buf1, buf2 = dumpbufs(buf1, buf2, len(buf1), len(buf2))
                break

            for i in range(max(len(buf1), len(buf2))):
                if i < len(buf2) and line1 == buf2[i]:
                    buf1, buf2 = dumpbufs(buf1, buf2, len(buf1), i+1)
                if i < len(buf1) and line2 == buf1[i]:
                    buf1, buf2 = dumpbufs(buf1, buf2, i+1, len(buf2))

diff('b.txt', 'a.txt')


# Задача 4
# Написать программу аналогичную tail, которая выводит
# последние 10 строк текстового файла, переданного на stdin

import sys
buf = []
for line in sys.stdin:
    buf.append(line)
    while len(buf) > 10:
        del buf[0]

for line in buf:
    print(line, end="")


# Задача 5
# Вывести все пятницы 13 в 2017-м году

from datetime import date
for month in range(12):
    d = date(2017, month+1, 13)
    if d.weekday() == 4:
        print(d)
