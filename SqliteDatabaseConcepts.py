import sqlite3
from student import Student

conn = sqlite3.connect('student.db')

c = conn.cursor()

#c.execute("""CREATE TABLE students(
#            first text,
#            last text,
#            pay integer
#            )""")

stu_1 = Student('Naman','Hirani',200000)

print(stu_1.first)
print(stu_1.last)
print(stu_1.fee)

#c.execute("INSERT INTO students VALUES ('Suhi','Kumar',2000)")
#conn.commit()

c.execute('SELECT * FROM students')
print(c.fetchall()) #USE TO PRINT THE RESULT

conn.commit()
conn.close()
