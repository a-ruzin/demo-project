# Задача 1
#
#  Сделать производный класс от dict, изменив поведение метода update так,
# чтобы он возвращал ссылку на экземпляр измененного словаря

class ExtendedDict(dict):
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        return self

d = ExtendedDict(key1=1, key2='value2')
d.update({'key3': 3}).update({'key4': 'value4'})
print(d, type(d))


# Задача 2
#
#  Спроектировать систему классов, описывающих работу сотрудников
# в компании с несколькими отделами. Сделать методы для отдела:
#  - список всех сотрудников 
# - суммарная зарплата всех сотрудников отдела. 
# У каждого отдела должен быть ровно один менеджер. Менеджер является
# сотрудником, но ему должен быть доступен список его подчиненных.
# Зарплата для обычных сотрудников это константа. Зарплата для Менеджера
# это константа + надбавка помноженная на количество подчиненных

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.department = None
    def get_salary(self):
        return self.salary
    def __str__(self):
        return "{}: {}".format(self.name, self.get_salary())

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def get_salary(self):
        return self.salary + len(self.department.employees) * self.bonus

class Department(object):
    def __init__(self, title):
        self.title = title
        self.employees = []
        self.manager = None
    def get_employees(self):
        return [self.manager] + self.employees
    def get_total_salary(self):
        return sum([e.get_salary() for e in self.get_employees()], 0)
    def set_manager(self, manager):
        self.manager = manager
        self.manager.department = self
    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self

d = Department('IT')
e1 = Employee('Ira', 100)
e2 = Employee('Olga', 110)
e3 = Employee('Petr', 90)
m = Manager('Vasya', 200, 10)
d.add_employee(e1)
d.add_employee(e2)
d.add_employee(e3)
d.set_manager(m)

print(d.get_total_salary())
for emp in d.get_employees():
    print(emp)
