import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

while True:
    print("\n1. Insert")
    print("2. View")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        cursor.execute("INSERT INTO student VALUES (?,?,?)", (id, name, marks))
        conn.commit()

    elif choice == 2:
        cursor.execute("SELECT * FROM student")
        data = cursor.fetchall()

        for row in data:
            print(row)

    elif choice == 3:
        break

conn.close()