import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=SQLSRV01\PRODUCCION;'
    'Database=PERS;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM MAESTROPERSONAL')

for i in cursor:
    print(i)
