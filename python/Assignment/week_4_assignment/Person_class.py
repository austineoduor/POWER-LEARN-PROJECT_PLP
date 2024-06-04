#!/usr/bin/python3

'''person class'''
class Person:
    '''
    The class presents person:
        name
        age
        gender
    '''
    def __init__(self,name,age,gender):
        '''class constructor'''
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        '''introduces a person'''
        return f"\nMy names are: {self.name}\n I am {self.age} years old\n And I am a {self.gender}"

if __name__ == "__main__":

    person = Person("John Doe",25,"Male")
    print(person.introduce())
