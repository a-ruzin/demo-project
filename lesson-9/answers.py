# Написать программу, которая перенесет информацию из файлов users.csv, views.csv
# из lesson-3 в базу данных sqlite. (Требуется создать соответствующие таблицы)

import sqlite3
import csv

with sqlite3.connect('db.sqlite') as conn:
    cur = conn.cursor()

    cur.execute('create table users (id, name, age)')
    with open('../lesson-3/users.csv', 'r') as csvfile:
        users_reader = csv.reader(csvfile, delimiter='\t')
        cur.executemany("insert into users values(?,?,?)", users_reader)

    cur.execute('create table views (url, user_id, duration)')
    with open('../lesson-3/views.csv', 'r') as csvfile:
        views_reader = csv.reader(csvfile, delimiter='\t')
        cur.executemany("insert into views values(?,?,?)", views_reader)


# Переписать задачу из lesson-3, чтобы программа получала данные из созданной
# базы данных, а не из файлов

import sqlite3

with sqlite3.connect('db.sqlite') as conn:
    cur = conn.cursor()

    cur.execute("""
        select
            round(age/10) as age_segment,
            count(*)
        from
            views JOIN users on user_id=id
        where
            url='b3e3e393c77e35a4a3f3cbd1e429b5dc'
        group BY
            age_segment
    """)

    segments = [0]*10
    for age_segment, cnt in cur:
        segments[round(age_segment)] = cnt

    for age_segment, cnt in enumerate(segments):
        print("{}-{}: {}".format(age_segment*10, age_segment*10+9, cnt))