import random
import string
import hashlib
import pandas as pd
from IPython.display import display, HTML
import pyodbc

h = hashlib.new('sha256')

# arrays for the username salt and hashed password
usernameArray = []
saltArray = []
hashedPasswordArray = []

# Declaring username and password
username = input('Enter your username: ')
password = input('Enter your password: ')

# Creating a salt

def getRandomString(length):
    # all characters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890123456789'
    results_str = ''.join(random.choice(letters) for i in range(length))
    return results_str

salt = getRandomString(20)

# Combining password and salt
saltedPassword = password + salt

# Converting password to a byte
bytePassword = bytes(saltedPassword, 'utf-8')

h.update(bytePassword)

hashedPassword = h.hexdigest()

# Appending the username, salt and hashed password to an array
usernameArray.append(username)
saltArray.append(salt)  
hashedPasswordArray.append(hashedPassword)

# storage into a csv/excel file, How in the fuck am i going to do that
# 1, that bitch is in a csv

# hashedPassword = encrypted password
# salt = The salt key

df = pd.DataFrame({'Username': usernameArray, 'Key': saltArray, 'Hash': hashedPasswordArray})

display(df)

# df.loc[len(df.index)] = [usernameArray, saltArray, hashedPasswordArray]

df.to_csv('password.csv', index=False, encoding='utf-8')

data = pd.read_csv (r'password.csv')
df = pd.DataFrame(data)

# if i insert into a database, everytime i run the script i can add one more row
# 8===D

## after this is storing into a database for fuck sakes

# Connection to my database (fuckin yeeted that code from CarProgram.py)
cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=JAIDENBUTLER-CA\SQLEXPRESS;"
            "Database=car;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

# Gotta make that cursor
cursor = cnxn.cursor()

# gotta insert that gay ass shit

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO loginData (username, salt, hash)
                VALUES (?,?,?)
                ''',
                row.Username,
                row.Key,
                row.Hash
    )
cnxn.commit()

cursor.close()
cnxn.close()