import pandas as pd
import hashlib
import pyodbc

h = hashlib.new('sha256')

# what i am going to do is run the hashing script and then validate
# using an if statement if the hashing algorithm matches the password
# given using the salt key as a hashing key

# getting the username and password to compare to the hashed version stored
username = ''
password = ''

username = input('Enter your username: ')
password = input('Enter your password: ')



data = pd.read_csv (r'password.csv')
df = pd.DataFrame(data)

cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=JAIDENBUTLER-CA\SQLEXPRESS;"
            "Database=car;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

# cursor = #cursed
cursor = cnxn.cursor()

userSearch = cursor.execute('SELECT Username, Salt, Hash FROM logindata WHERE Username = ?', username)

rows = userSearch.fetchall()

if len(rows) == 0:
    print('Username or Password not found')
else:
    for row in rows:
#        print(f'{row.Username} {row.Salt} {row.Hash}')
        dataUsername = row.Username
        dataSalt = row.Salt
        dataHash = row.Hash
    # exit the for loop gang gang 
# Hashing the password given
    saltedPassword = password + dataSalt

# Converting password to a byte
    bytePassword = bytes(saltedPassword, 'utf-8')

    h.update(bytePassword)

    hashedPassword = h.hexdigest()

    print(hashedPassword)


    if hashedPassword == dataHash:
        print('Password is correct')
    else:
        print('Password is incorrect')