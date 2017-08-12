#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USER = 'root'
PASSWORD = 'password'
SERVER = 'localhost'
PORT = 3306
DB = 'test'


Base = declarative_base()

class User(Base):
    __table_name__ = 'tmp_usr'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    books = relationship('Book')
    
class Book(Base):
    __table_name__ = 'tmp_book'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user_id = Column(Integer, ForeignKey('tmp_user.id'))

engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%d/%s' % (USER, PASSWORD, SERVER, PORT, DB))
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id=5, name='Allen')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id == 5).one()
print('Object type of:', type(user))
print('Query result: name ->', user.name)
session.close()

session = DBSession()
new_book0 = Book(id=1, name='Python', user_id=5)
new_book2 = Book(id=2, name='Java', user_id=5)
new_book3 = Book(id=3, name='C#', user_id=5)
session.add(new_book0)
session.add(new_book1)
session.add(new_book2)
session.commit()

books = session.query(Book).filter(Book.user_id == 5).all()
print('Query result: books ->', [book for book in books])
session.close()