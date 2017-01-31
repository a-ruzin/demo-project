from abc import ABCMeta, abstractmethod

class A:
    @abstractmethod
    def spam(self):
        print('qqq')

a = A()
a.spam()


import random

x = list(range(10))
y = x
print(x, y, x is y)
random.shuffle(x)
print(x, y, x is y)

import sys

print(sum([random.gauss(0, 1) for x in range(100000)]))
print(sys.argv)
