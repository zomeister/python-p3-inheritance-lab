#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        pass
    
    def learn(self, my_str):
        self.knowledge.append(my_str)
        pass