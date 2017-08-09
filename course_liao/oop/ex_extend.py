# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self):
        print("This is a", self.__class__.__name__, '.')

class Mammal(Animal):
    def __init__(self):
        print("This is a", self.__class__.__name__, 'animal.')

class Bird(Animal):
    def __init__(self):
        print("This is a", self.__class__.__name__, 'animal.')

class Runnable(object):
    def run(self):
        print("See, it's running now.")

class Flyable(object):
    def fly(self):
        print("See, it's flying now.")

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

class Parrot(Bird, Flyable):
    pass

dog = Dog()
bat = Bat()
ostrich = Ostrich()
parrot = Parrot()

dog.run()
bat.fly()
ostrich.run()
parrot.fly()