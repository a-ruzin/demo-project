import random
import hashlib

first_names = ['Maria', 'Olga', 'Eugenia', 'Svetlana', 'Penny']
last_names = ['Ivanova', 'Petrova', 'Sidorova', 'Alekseeva', 'Borisova', 'Sergeeva', 'Vladimirova']


def get_random_name():
    first_name = first_names[random.randint(0, len(first_names) - 1)]
    last_name = last_names[random.randint(0, len(last_names) - 1)]
    return "{} {}".format(first_name, last_name)


with open('users.csv', 'w') as f:
    for u in xrange(100):
        print >>f, "{}\t{}\t{}".format(u, get_random_name(), random.randint(10, 99))


with open('views.csv', 'w') as f:
    for u in xrange(10000):
        print >>f, "{}\t{}\t{}".format(hashlib.md5(str(random.randint(0, 200))
                                                   ).hexdigest(), random.randint(0, 99), random.randint(0, 10))
