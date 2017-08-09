# -*- coding: utf-8 -*-

class Animal(object):
    
    def say(self):
        print("I'm a ", object)
    
    def run(self):
        print('Animal is running...')

class Dog(Animal):
 
    def run(self):
        print("Hey, look it, I 'm running now.")

class Cat(Animal):

    def run(self):
        print("I'm very tried, i won't run.")

    def catch(self,hasMouse):
        if hasMouse:
            print("I saw the mouse, I will catch it.")
        else:
            print("There found not mouse.")


dog = Dog()
mouse = Animal()
cat = Cat()

dog.say()
dog.run()

mouse.say()
mouse.run()

cat.say()
cat.run()
cat.catch(True)

print(type(dog))
print(type(mouse))
print(type(None))

print('The dog is a animal? ', isinstance(dog, Animal))