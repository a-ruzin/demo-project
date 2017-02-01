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

something_wrong(1, 2, key=34)