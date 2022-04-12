# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:20:8 2022

@author: 20CE013
"""
"""
AIM :
    
Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result.

The Student class has data members such as those representing rollNumber, Name, etc.

Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six
subjects. Derive Result from the Exam class, and it has its own fields such as total_marks.

Write an interactive program to model this relationship.

https://github.com/Mayank7011/Practical

"""


class Student:
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name
    
    def display(self):
        print(f'Student Roll No: {self.rollNo}')
        print(f'Student Name: {self.name}')

class Exam(Student):
    def __init__(self, rollNo, name, subject):
        super().__init__(rollNo, name)
        self.subject = subject
    
    def display(self):
        super().display()
        for i in range(len(self.subject)):
            print(f'Subject {i} Marks: {self.subject[i]}')

class Result(Exam):
    total_marks = 0
    def __init__(self, rollNo, name, subject):
        super().__init__(rollNo, name, subject)
        self.total_marks = sum(subject)
    
    def display(self):
        super().display()
        print(f'Total Marks: {self.total_marks}')


if __name__ == '__main__':
    student = Student(1, 'Mayank')
    student.display()
    print()

    exam = Exam(2, 'Jay', [10, 20, 30])
    exam.display()
    print()

    result = Result(3, 'Dhruv', [40, 50, 60])
    result.display()
    print()
