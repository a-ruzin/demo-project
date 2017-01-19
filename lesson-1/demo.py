a = 3

def f():
    b = 4
    global a
    print('-', a, b)
    a += 3

    def f2():
        nonlocal b
        global a
        print('+', a, b)
        b = 3
        a += 3

    f2()

f()

print(a)


def callf(func):
    return func()

x = 37
def helloworld():
    return "Привет, Мир! x = % d" % x

print(callf(helloworld))
x = 38
print(callf(helloworld))
