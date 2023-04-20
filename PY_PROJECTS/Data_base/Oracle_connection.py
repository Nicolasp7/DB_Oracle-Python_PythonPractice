import cx_Oracle

try:
    conexion = cx_Oracle.connect(
        password='Saavedra.010',
        user='system',
        dsn='localhost/xe')
except Exception as err:
    print('DB connection has failed', err)
else:
    print('DB Oracle Connection Succesfully', conexion.version)

# cur_01 = conexion.cursor()
# cur_01.execute('select * from dual')
# result = cur_01.fetchall()
# print(result)

# Create
# create_table = '''create table prove(
# field1 varchar(40),
# field2 int not null)'''
# cur_01.execute(create_table)

# Insert Registers
try:
    cur_01 = conexion.cursor()
    insert_data= '''insert into prove values (
    'first code', 1001)'''
    cur_01.execute(insert_data)
except Exception as err:
    print('Mistake inserting data')
else:
    print('Inserting Data Correct')
    conexion.commit()

conexion.close()

