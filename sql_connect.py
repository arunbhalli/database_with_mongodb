import pyodbc
conn = pyodbc.connect(
 'Driver={SQL Server};'
 'Server=LAPTOP-TL0L7VAA\MSSQLSERVER01;'
 'Database=menu;'
 'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM menu')
for i in cursor:
 print(i)

