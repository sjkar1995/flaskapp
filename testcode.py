import pyodbc
import pandas as pd
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-GJ0PM7F\SQLEXPRESS;'
                      'Database=test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM customer')

for i in cursor:
    print(i)
