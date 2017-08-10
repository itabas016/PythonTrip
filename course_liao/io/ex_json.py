# -*- coding: utf-8 -*-

import json


d = dict(name='Bob', age=20, score=90)
data = json.dumps(d)
print('JSON data is a str: ', data)

reborn = json.loads(data)
print('Load new json object: ', reborn)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 90)

#print(json.dumps(s))
print('Dump Student: ', json.dumps(s, default=lambda obj: obj.__dict__))

data = json.dumps(s, default=lambda obj: obj.__dict__)

print('Rebuild Student: ', json.loads(data, object_hook=lambda d: Student(d['name'], d['age'], d['score'])))

