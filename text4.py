import sqlite3
#connect to database 
conn = sqlite3.connect("student.db")
#create cursor
cursor = conn.cursor()
#create table
cursor.execute("""
        CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY,
        name TEXT,
        mmarks INTEGER)""")
#insert data
cursor.execute("INSERT INTO student VALUES (1,'Amit',80)")
cursor.execute("INSERT INTO student VALUES (2,'Neha',90)")
cursor.execute("INSERT INTO student VALUES (3,'Ravi',75)")
conn.commit()
cursor.execute("SELECT*FROM student")
rows=cursor.fetchall()
print("Student Recorded:")
for row in rows:
    print(row)
    conn.close