users = {}
try:
    with open('users.csv', 'r') as views_file:
        for line in views_file:
            _id, name, age = line.strip().split('\t')
            users[_id] = {'name': name, 'age': int(age)}
except Exception:
    print('bad file users.csv')

print(users)

goods = {}
try:
    with open('views.csv', 'r') as views_file:
        for line in views_file:
            url, user_id, duration = line.strip().split('\t')
            if url in goods:
                goods[url].add(user_id)
            else:
                goods[url] = {user_id}

except Exception:
    print('bad file views.csv')

print(goods)

URL = '6f4922f45568161a8cdf4ad2299f6d23'
# print [users[x]['age'] for x in goods[URL]]


def print_dispersion(url):
    ranges = [0] * 11

    for user in goods[url]:
        ranges[users[user]['age'] // 10] += 1
    for i, r in enumerate(ranges):
        print('{}-{}: {}'.format(i * 10, i * 10 + 9, r))


for url in goods:
    print('-'*100)
    print(url)
    print_dispersion(url)

