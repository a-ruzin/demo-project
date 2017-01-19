# Задача 1.
#
# Дан список целых чисел, например: [5, 13, 23, 32, 16, 1]
# Требуется напечатать минимальное и максимальное числа из этого списка.

a = [5, 13, 23, 32, 16, 1]
print(min(a), max(a))


# Задача 2.
#
# Вывести все числа Фибоначи меньше 1000
# Числа Фибоначи образуются путем сложения двух предыдущих чисел.
# При этом первые два числа равны единице: 1, 1, 2, 3, 5, 8, ...

fib = []
while True:
    if len(fib) < 2:
        fib.append(1)
    else:
        new_fib = fib[-1] + fib[-2]
        if new_fib < 1000:
            fib.append(new_fib)
        else:
            break

print(fib)


# Задача 3.
#
# Дана строка a="PYTHON", необходимо напечатать строку, где буквы идут задом наперед

a = "PYTHON"
print(a[::-1])


# Задача 4.
#
# Напечатать все простые числа меньше 1000

simple = [2]
for x in range(3, 1000, 2):
    for t in simple:
        if not x % t:
            break
    else:
        simple.append(x)
print(simple)


# Задача 5.
#
# Напечатать все простые числа Фибоначи меньше 1000

print(sorted(list(set(fib) & set(simple))))


# Задача 6.
#
# Дана произвольная строка.
# Найти и напечатать самый длинный фрагмент этой строки,
# который встречается больше одного раза (фрагменты не должны пересекаться)

def get_biggest_repetition(a):
    l = len(a)
    cl = len(a) // 2
    while cl > 0:
        luft = l - cl*2
        for x in range(1+luft):
            s1 = a[x:x+cl]
            for y in range(1-x + luft):
                s2 = a[x+cl+y:x+cl+y+cl]
                if s1 == s2:
                    return s1
        cl -= 1

print(get_biggest_repetition("абвгдежзиклмнопрстуфх") or "нет повторений")
print(get_biggest_repetition("это произвольная строка") or "нет повторений")
