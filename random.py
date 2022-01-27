import random
import sqlite3
import time

start = time.time()

random_list = [(random.randint(10, 25),) for num in range(100000)]

connection = sqlite3.connect('original.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE pressure ( 
reading INTEGER
);''')

cursor.executemany('''INSERT INTO pressure (reading)
VALUES(?);''', random_list)

cursor.close()
connection.commit()
connection.close()

end = time.time()
print(start - end)