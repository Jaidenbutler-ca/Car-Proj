import pandas as pd
import hashlib
import pyodbc

# what i am going to do is run the hashing script and then validate
# using an if statement if the hashing algorithm matches the password
# given using the salt key as a hashing key

data = pd.read_csv (r'password.csv')
df = pd.DataFrame(data)

cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=JAIDENBUTLER-CA\SQLEXPRESS;"
            "Database=car;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

# cursor = #cursed
cursor = cnxn.cursor()

# this might be the script??????????????????????
