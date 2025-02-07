# Program Name: Assignment2.py 
# Course: IT3883/Section W02
# Student Name: Leonardo Barranco
# Assignment Number: Lab2
# Due Date: 2/7/2025
# Purpose: This program has the code go to a file
# input the data and calculate the averages of the groups and put them in order 
# https://www.freecodecamp.org/news/python-sort-list-how-to-order-by-descending-or-ascending/
#https://stackoverflow.com/questions/30355023/getting-an-average-from-a-text-file

with open('input.txt', 'r') as file:
    
    #This calculates the final averages
    students = []
    for line in file:
        data = line.split()
        name = data[0]
        scores = list(map(int, data[1:]))
        average = sum(scores) / len(scores)
        students.append((name, average))
    
    #This sorts and prints the resluts
    students = sorted(students, key=lambda x: x[1], reverse=True)
    for student in students:
        print(f'{student[0]} {student[1]:.2f}')