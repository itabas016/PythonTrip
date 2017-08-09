# -*- coding: utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
    
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self.__score = value

s = Student()
s.score = 60
print(s.score)

try:
    s.score = 1000
except ValueError as identifier:
    print(identifier)


class Screen(object):

    #__slots__ = ('__width', '__height', '__resolution')
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def resolution(self):
        if self.__width == 0 or self.__height == 0:
            raise ValueError("The input parameter value can't be zero")
        else:
            print(self.__width, '*', self.__height, '=', self.__width * self.__height)
            return self.__width * self.__height

s = Screen()
s.width = 1024
s.height = 768
s.name ='test screen'
print(s.name)
print(s.resolution)
