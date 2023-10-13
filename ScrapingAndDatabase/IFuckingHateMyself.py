# Test Worked
# Time to Run to 100: 1:30.00
# 277.78% more efficient

# Desktop SQL Server Location: DESKTOP-H10UUI9\SQLEXPRESS
# Desktop car.csv location: C:\Users\School\OneDrive - NAIT\Documents\GitHub\Car-Proj\car.csv
#

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc
import concurrent.futures
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
    "Whitecourt,",
]
fullDealerString = []

# Working here
# Working here
# Working here

def scrape_page(page_number):
    url = f"https://www.carpages.ca/used-cars/search/?num_results=50&province_code=ab&p=={page_number}"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, "html.parser")
    results = soup.find(id="")
    car_elements = results.find_all("div", class_="media__content")

    for car_element in car_elements:
        price_element = car_element.find("strong", class_="delta")
        name_element = car_element.find("a", class_="")
        price.append(price_element.text.strip())
        name.append(name_element.text.strip())
        print(page_number)

    location_elements = results.find_all("div", class_="l-column l-column--large-4 grey vehicle__card--dealer")

    for location_element in location_elements:
        dealer_element = location_element.find("h5", class_="hN")
        city_element = location_element.find("p", class_="hN")
        dealer.append(location_element.text.strip())
        city.append(city_element.text.strip())
        print(page_number)

with concurrent.futures.ThreadPoolExecutor() as executor:
    page_number = range(1,50)
    executor.map(scrape_page, page_number)
    print(page_number)

#  with concurrent.futures.ThreadPoolExecutor() as executor:
#    page_number = range(51,100)
#    executor.map(scrape_page, page_number)
#    print(page_number)

df = pd.DataFrame({'price': price, 'name': name, 'dealer': dealer, 'city': city})
df.to_csv('car.csv', index=False, encoding='utf-8')

# all the data cleaning goes on here

# Getting the CSV file
data = pd.read_csv (r'C:\Users\School\OneDrive - NAIT\Documents\GitHub\Car-Proj\car.csv')
df = pd.DataFrame(data)

fullDealerString = df["dealer"]

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

df["dealer"] = df["dealer"] + " " + fourthWord


# connecting to SQL database
cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=DESKTOP-H10UUI9\SQLEXPRESS;"
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

