# Задача 1
# Найти наименьшее число фибоначи, которое делится на заранее
# заданное число без остатка. При решении использовать генераторы

def fibbonachi():
    fibs = 0, 1
    while True:
        yield fibs[1]
        fibs = fibs[1], sum(fibs)

N = 100
for i, fib in enumerate(fibbonachi()):
    if i > 1000:
        print("too big number")
        break
    if fib % N == 0:
        print("found: {} at {}'th place".format(fib, i+1))
        break
