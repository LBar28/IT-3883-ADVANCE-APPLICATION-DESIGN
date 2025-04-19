# Program Name: Assignment5
# Course: IT3883/Section W02
# Student Name: Leonardo Barranco
# Assignment Number: Lab5
# Due Date: 4/18/2025
# Purpose: This program teaches us how to create a database, insert data into it, and take out data. 
#https://www.geeksforgeeks.org/python-sqlite/

import sqlite3

def create_database_and_table():
    connection = sqlite3.connect('temperature_data.db')
    cursor = connection.cursor()

#creating the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TemperatureData (
            ID INTEGER PRIMARY KEY,
            Day_Of_Week TEXT,
            Temperature_Value REAL
        )
    ''')

    connection.commit()
    return connection, cursor  # return both so they can be reused

# Read data from a file and insert into the database
def insert_data_from_file(cursor, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            day_of_week = data[0]
            temperature_value = float(data[1])

            cursor.execute('''
                INSERT INTO TemperatureData (Day_Of_Week, Temperature_Value)
                VALUES (?, ?)
            ''', (day_of_week, temperature_value))

# Compute and print the average temperature for specified days
def compute_average_temperature(cursor, days):
    for day in days:
        cursor.execute('''
            SELECT AVG(Temperature_Value)
            FROM TemperatureData
            WHERE Day_Of_Week = ?
        ''', (day,))
        avg_temp = cursor.fetchone()[0]
        print(f"Average temperature for {day}: {avg_temp:.2f}°F")



connection, cursor = create_database_and_table()
insert_data_from_file(cursor, 'temp.txt')
connection.commit()

compute_average_temperature(cursor, ['Sunday', 'Thursday'])

connection.close()
