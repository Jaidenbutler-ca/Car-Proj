import pyodbc

makeVariable = '%'
modelVariable = '%'
yearVariable = '%'

# connecting to SQL database
cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=DESKTOP-H10UUI9\SQLEXPRESS;"
            "Database=car;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
# establishing a cursor
cursor = cnxn.cursor()

cursor.execute("DECLARE @make AS VARCHAR(100)='%'")
cursor.execute("DECLARE @model AS VARCHAR(100)='%'")
cursor.execute("DECLARE @year AS VARCHAR(4)='%'")

cursor.execute("SELECT * FROM info WHERE make LIKE ? AND name LIKE ? AND year LIKE ?", makeVariable, modelVariable, yearVariable)



for row in cursor:
    print(row)


cursor.close()
cnxn.close()
