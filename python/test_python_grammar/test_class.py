#-*- coding: utf-8 -*-

# author: li yangjin

class Student(object):
    count = 0

    def __init__(self, name):
        self.__name = name
        Student.count = Student.count + 1

    def get_name(self):
        return self.__name


A = Student("Bob")
# print(A.__name)
print (A.get_name())
print(A._Student__name)

class Animal(object):
    def run(self):
        print("Animal is running")

class Dog(Animal):
    def run(self):
        print("Dog is running")

animal = Animal()
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Animal())

class Timer(object):

    def run(self):
        print('Start...')


run_twice(Timer())