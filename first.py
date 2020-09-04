# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class student:
    def __init__(self,roll_no,age):
        self.roll_no=roll_no
        self.age=age
    def __str__(self):   
        return f"roll_no {self.roll_no} at age of {self.age}"
x=student(1,18)
print(x)