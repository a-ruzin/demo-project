from abc import ABCMeta, abstractmethod

class A:
    @abstractmethod
    def spam(self):
        print('qqq')

a = A()
a.spam()


class C(metaclass=ABCMeta):
    @abstractmethod
    def c(self):
        pass

c = C()

c.c()
