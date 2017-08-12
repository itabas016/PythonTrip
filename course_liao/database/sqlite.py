#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sqlite3

db = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db):
    os.remove(db)

conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute('create table tmp (id varchar(20) primary key, name varchar(50))')
cursor.execute('insert into tmp (id, name) values (\'1\', \'itabas\')')

cursor.rowcount
cursor.close()
conn.commit()

cursor = conn.cursor()
cursor.execute('select * from tmp where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()

cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()

conn.close()

def get_score_in(low, high):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('select name from user where score between :p1 and :p2 order by score asc', (low, high))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    print('%s, get score in (%d, %d)' % ([value[0] for value in values], low, high))

get_score_in(80, 95)
get_score_in(60, 80)
get_score_in(60, 100)