#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()
cursor.execute('create table tmp_user (id integer primary key, name varchar(20))')
cursor.execute('insert into tmp_user (id, name) values (s%, %s)', [1, 'itabas'])
cursor.rowcount
cursor.close()
conn.commit()


cursor = conn.cursor()
cursor.execute('select * from user where id = %s;', 1)
values = cursor.fetchall()
cursor.close()
conn.close()
print(values)
