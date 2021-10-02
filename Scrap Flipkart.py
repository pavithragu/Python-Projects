import requests
from bs4 import BeautifulSoup
import pandas as ps
import os

# Ask the user to type the product name
product = input("Enter the product name: ")

# Convert the data as Flipkart link
query = "https://www.flipkart.com/search?q=" + product

# get the page of product's search result
data = requests.get(query)

# convert and store the html data as python object
obj = BeautifulSoup(data.content, features="html.parser")

# empty lists to sore Name, Price & Specifications
a, b, c = [], [], []

# for-loop to get all the values from the html data
for g in obj.findAll():
    name = g.find('div', attrs={'class': '_4rR01T'})
    price = g.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    spec = g.find('div', attrs={'class': 'fMghEO'})

    # Append the values to the lists
    if name and price and spec is not None:
        a.append(name.text)
        b.append(price.text[1:])
        c.append(spec.text)

if len(a) != 0:
    # store the data in csv file
    df = ps.DataFrame({'Product Name': a, 'Price': b, 'Specifications': c})
    df.to_csv('product_details.csv', index=False, encoding="utf-8")
    os.system("product_details.csv")

else:
    for g in obj.findAll():
        name = g.find('a', attrs={'class': "s1Q9rs"})
        price = g.find('div', attrs={'class': '_30jeq3'})

        # Append the values to the lists
        if name and price is not None:
            a.append(name.text)
            b.append(price.text[1:])

    if len(a) != 0:
        # store the data in csv file
        df = ps.DataFrame({'Product Name': a, 'Price': b})
        df.to_csv('product_details.csv', index=False, encoding="utf-8")
        os.system("product_details.csv")

    else:
        print("No data found")
