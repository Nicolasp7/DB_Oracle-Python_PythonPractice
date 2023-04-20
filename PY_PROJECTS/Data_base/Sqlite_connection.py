import sqlite3
connection = sqlite3.connect('Base1')  # Creation DB

#  DB Editor from sqlite
#  Cursor

cursor01 = connection.cursor()
# cursor01.execute('''create table user(
#                   name varchar (20),
#                   age int,
#                   direction varchar(50),
#                   telef numeric(10))''')

# cursor01.execute("insert into user values('MrCause', 33, 'Fortezza 3', 1234567)")

# Insert Lists 
mas_user = [
    ('Cause', 34, "3 fortezza", 12345609),
    ('Anderson', 31, "3fortezza3", 87612345609),
    ('Causa', 30, "tresfortezza3", 858439)
]
cursor01.executemany('insert into user values(?,?,?,?)', mas_user)

connection.commit()

connection.close()
