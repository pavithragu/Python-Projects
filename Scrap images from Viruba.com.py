from bs4 import BeautifulSoup
import requests
import re
from time import sleep
import os
import pandas

# Getting Page Source of Viruba.com
request = requests.get("http://www.viruba.com/categories.aspx")
source = BeautifulSoup(request.content, features="html.parser")

# Empty dictionary to store the book details
books = {}


# Creating a function
def save_images():
    # File Name for the downloading images
    filename = 100000

    # Get the table tag from the source html
    for category in source.findAll("table"):

        # Get the individual links and names of Categories
        for i in category.findAll("a", href=True):

            # Creating variables for Category name and link
            category_name = i.text
            category_link = "http://www.viruba.com/" + i["href"]

            # Creating Folder with a name of Category
            try:
                os.makedirs(f"/VirubaImages/{category_name}")
            except:
                pass

            # Getting the Source of Individual Categories
            book_request = requests.get(category_link)
            book_source = BeautifulSoup(book_request.content, features="html.parser")

            # Get the table tag from the source html
            for book_detail in book_source.findAll("table", attrs={"id": "MainContent_DataGridBooks"}):

                # Get the individual links and names of Book
                for each in book_detail.findAll("img", title=True, src=True):
                    # Store the Name link of the book in each variables
                    book_name = (each["title"]).strip()
                    book_link = "http://www.viruba.com/" + each["src"]

                    # Print the status of download
                    print("Downloading:", category_name + "/" + book_name + ".jpg")

                    # Download the images to the specific location with its name
                    filename += 1
                    image = open(f"/VirubaImages/{category_name}/{filename}.jpg", "wb")
                    book_image = requests.get(book_link)
                    image.write(book_image.content)

                    # Add the values to the dictionary
                    books[filename] = (book_name, book_link, category_name, category_link)

                    # Show the Details
                    print(filename, ":", books[filename])
                    print()


# Calling the function()
save_images()
