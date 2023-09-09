# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE IF NOT EXISTS Students(
Student_Id  Integer, 
Student_Name  Text, 
School_Id  Integer Primary key);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """INSERT INTO Students(Student_Id, Student_Name, School_Id)
VALUES
(201, 'Иван', 1),
(202, 'Петр', 2),
(203, 'Анастасия', 3),
(204, 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()


def get_teacher_data(Student_id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sqlquery = 'SELECT * FROM Students JOIN School ON Students.School_id = School.School_id WHERE Students.Student_id = ?'
    cursor.execute(sqlquery, (Student_id,))
    student_info = cursor.fetchall()
    for row in student_info:
      print ("ID Студента:", row[0])
      print ("Имя Студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", row[4], '\n')
      
    close_connection(con)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка вида ", error)

get_teacher_data(201)
get_teacher_data(202)
get_teacher_data(203)
get_teacher_data(204)

