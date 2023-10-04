import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc
global x
global thirdWord
global fourthWord

page_number = 1

name = []
price = []
year = []
make = []
dealer = []
city = []
thirdWord = []
alberta_towns = [
    "Calgary,",
    "Edmonton,",
    "Edmonton",
    "Red Deer,",
    "Lethbridge,",
    "Fort McMurray,",
    "Medicine Hat,",
    "Grande Prairie,",
    "Airdrie,",
    "Spruce Grove,",
    "Sherwood Park,",
    "St. Albert,",
    "Leduc,",
    "Camrose,",
    "Lloydminster,",
    "Brooks,",
    "Okotoks,",
    "Coaldale,",
    "Canmore,",
    "Hinton,",
    "Wetaskiwin,",
    "Lacombe,",
    "Vermilion,",
    "Sherwood",
    "Park,",
    "AB",
    "Medicine",
    "Pincher",
    "Creek,",
]
fullDealerString = []

while page_number <= 100:
    URL = f"https://www.carpages.ca/used-cars/search/?num_results=50&province_code=ab&p=={page_number}"
    page = requests.get(URL)
    print(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="")
    car_elements = results.find_all("div", class_="media__content")

    for car_element in car_elements:
        price_element = car_element.find("strong", class_="delta")
        name_element = car_element.find("a", class_="")
        price.append(price_element.text.strip())
        name.append(name_element.text.strip())

    location_elements = results.find_all("div", class_="l-column l-column--large-4 grey vehicle__card--dealer")

    for location_element in location_elements:
        dealer_element = location_element.find("h5", class_="hN")
        city_element = location_element.find("p", class_="hN")
        dealer.append(location_element.text.strip())
        city.append(city_element.text.strip())

    page_number += 1

df = pd.DataFrame({'price': price, 'name': name, 'dealer': dealer, 'city': city})
df.to_csv('car.csv', index=False, encoding='utf-8')

fullDealerString = df["dealer"]

# Getting the CSV file
data = pd.read_csv (r'C:\Users\jaide\OneDrive\Desktop\Python_VSCode\car.csv')
df = pd.DataFrame(data)

# splitting year from substring
df["year"] = df["name"].str.split().str[0]
year.append(df["year"])

# getting rid of year compleatly
df["name"] = (df["name"].str.split().str[1]) + " " + (df["name"].str.split().str[2])

# splitting the make
df["make"] = df["name"].str.split().str[0]
make.append(df["make"])

# getting rid of make
df["name"] = df["name"].str.split().str[1]

# getting the third word of the dealer field into an array
thirdWord = df["dealer"].str.split().str[2]
df["dealer"] = df["dealer"].str.split().str[0] + " " + df["dealer"].str.split().str[1]

# Declaring the Fourth Word
fourthWord = fullDealerString.str.split().str[3]

for x in thirdWord:
    thirdWord = thirdWord.replace(alberta_towns, " ")
    fourthWord = fourthWord.replace(alberta_towns, " ")


df["dealer"] = df["dealer"] + " " + thirdWord

#
# Working Here!
#

df["dealer"] = df["dealer"] + " " + fourthWord

# connecting to SQL database
cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=Jaidenbutler-ca\SQLEXPRESS;"
            "Database=car;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
# establishing a cursor
cursor = cnxn.cursor()
# Dropping the old info from the table
cursor.execute("DELETE FROM info")

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO info (price, year, make, name, dealer, city)
                VALUES (?,?,?,?,?,?)
                ''',
                row.price,
                row.year,
                row.make,
                row.name,
                row.dealer,
                row.city
    )
cnxn.commit()


# displaying Results in console
# cursor.execute("SELECT * FROM info")
#  = cursor.fetchall()
# for row in results:
#    print(row)

#closing the connection
cursor.close()
cnxn.close()

