import random
import hashlib

first_names = ['Maria', 'Olga', 'Eugenia', 'Svetlana', 'Penny']
last_names = ['Ivanova', 'Petrova', 'Sidorova', 'Alekseeva', 'Borisova', 'Sergeeva', 'Vladimirova']


def get_random_name():
    first_name = first_names[random.randint(0, len(first_names) - 1)]
    last_name = last_names[random.randint(0, len(last_names) - 1)]
    return "{} {}".format(first_name, last_name)


with open('users.csv', 'w') as f:
    for u in range(100):
        print("{}\t{}\t{}".format(u, get_random_name(), random.randint(10, 99)), file=f)


with open('views.csv', 'w') as f:
    for u in range(10000):
        print("{}\t{}\t{}".format(hashlib.md5(str(random.randint(0, 200)).encode()).hexdigest(),
                                  random.randint(0, 99),
                                  random.randint(0, 10)),
              file=f)
