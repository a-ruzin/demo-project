# Задача 1.
#
# Есть словарь вида: {'c': 4, 'k': 1, 'm': 7, ...}
# Требуется вывести ключи в порядке увеличения соответствующих им значений.

a = {'c': 4, 'k': 1, 'm': 7}
res = {}
for key, value in a.items():
    if key not in res:
        res[key] = [value]
    else:
        res[key].append(value)
for value, keys in res.items():
    print(keys)


# Задача 2.
#
# Написать функцию вычисления факториала n! без использования инструкции if, for, while
# n! = 1*2*3*...*n

def factorial(n):
    return n < 2 and 1 or n*factorial(n-1)

print(factorial(3))
print(factorial(6))
print(factorial(10))


# Задача 3.
#
# Написать простой калькулятор вычисляющий выражение для исходной строки вида:
# s = "3+7-1/5+3*6"
# Все числа состоят из одной цифры. Приоритетов у операций +,-,/,* - т.е. выполняются
# по мере появления (как если бы мы считали на обычном калькуляторе).
# Операции +,-,/,* оформить в виде классов.

class Operation():
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def calc(self):
        return None

    def calc_a(self):
        if isinstance(self.a, Operation):
            return self.a.calc()
        else:
            return self.a

    def calc_b(self):
        if isinstance(self.b, Operation):
            return self.b.calc()
        else:
            return self.b

class Plus(Operation):
    def calc(self):
        return self.calc_a() + self.calc_b()

class Minus(Operation):
    def calc(self):
        return self.calc_a() - self.calc_b()

class Multiply(Operation):
    def calc(self):
        return self.calc_a() * self.calc_b()

class Divide(Operation):
    def calc(self):
        return self.calc_a() / self.calc_b()


def parse(equation):
    a = int(equation[0])
    for i in range(1, len(equation), 2):
        op = equation[i]
        b = int(equation[i+1])
        if op == '+':
            a = Plus(a, b)
        elif op == '-':
            a = Minus(a, b)
        elif op == '*':
            a = Multiply(a, b)
        elif op == '/':
            a = Divide(a, b)
    return a

print(parse("3+7-1/5+3*6").calc())