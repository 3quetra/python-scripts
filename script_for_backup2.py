import sqlite3
import time
import os

os.remove('backup.db')
connection = sqlite3.connect('backup.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE pressure(
    reading INTEGER 
);''')

connection2 = sqlite3.connect('original.db')
cursor2 = connection2.cursor()

start = time.time()
numbers = cursor2.execute('SELECT * FROM pressure').fetchall()
numbers = [num for num in numbers if num[0] > 20]
end = time.time()
print(end - start, len(numbers))

cursor.executemany('''INSERT INTO pressure 
VALUES (?);''', numbers)

cursor2.close()
connection2.close()

cursor.close()
connection.commit()
connection.close()

