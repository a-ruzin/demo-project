import sqlite3

conn = sqlite3.connect('file.db')
with sqlite3.connect("file.db") as conn, sqlite3.connect("file.db") as conn2:
    cur = conn.cursor()

    # cur.execute("drop table user")
    # cur.execute("create table user (id integer PRIMARY KEY, name TEXT, year INTEGER)")
    # cur.execute("create UNIQUE index user_year on user (year)")
    # cur.execute("insert into user values(?, ?, ?)", (None, 'Mary', 1994))
    # cur.execute("drop table user")


    # users = [
    #     ('Pavel', 1995),
    #     ('Kirill', 1999)
    # ]
    # cur.executemany("insert into user (name, year) values(?, ?)", users)


    # посмотреть только что вставленный id
    # res = cur.execute("insert into user values(?, ?, ?)", (None, 'Olga', 1997))
    # print(res.lastrowid)


    # cur.execute("select * from user")
    # while True:
    #     row = cur.fetchone()
    #     if not row:
    #         break
    #     id, name, year = row
    #     print(id, name, year)

    # cur.execute("select * from user")
    # for _id, name, year in cur:
    #     print(_id, name, year)


    # cur.execute("select * from user where year >= ?", (1996,))
    # for _id, name, year in cur:
    #     print(_id, name, year)


    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    #
    # cur.execute("select id, name, year from user")
    # for row in cur:
    #     print(row['id'], row['name'], row['year'])


    # print('-'*50)
    #
    # cur.execute("select id, name, year from user")
    # for _id, name, year in cur:
    #     print(_id, name, year)
    #
    # conn.row_factory = None
    # cur = conn.cursor()


    # cur.execute("select id, name, year from user")
    # rows = cur.fetchall()
    # print(rows)


    # res = cur.execute("insert into user values(?, ?, ?)", (None, 'Sophie', 1988))
    # print(res.lastrowid)
    #
    # cur.execute("select id, name, year from user")
    # rows = cur.fetchall()
    # print(rows)
    #
    # raise Exception()


    # cur.execute("delete from user")


    # cur.execute("insert into user values(?, ?, ?)", (None, 'Mary', 1977))
    # cur.execute("select name, min(year) as min_year from user group by name")
    # rows = cur.fetchall()
    # print(rows)
