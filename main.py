import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm

while True:
    url = input("Enter a URL: ")
    if requests.get(url).status_code != 200:
        print("Invalid URL")
    else:
        break

# get the html from the url
request_url = urllib.request.urlopen(url)
html_doc = request_url.read()
soup = BeautifulSoup(html_doc, 'html.parser')
html_doc = soup.prettify()
print("Document found, now getting all text ")
# get just the text from the html
text = soup.find_all('p')
# write the text var to a file
with open('text.txt', 'w',encoding="utf-8") as f:
    for i in text:
        f.write(i.get_text())


# get the data from the table
if soup.find_all('tr'):
    tables = soup.find_all('tr')
    # write the text var to a file
    with open('table.txt', 'w',encoding="utf-8") as f:
        for i in tables:
            f.write(i.get_text())


# Save the files
while True:
    save = input("Do you want to save the text to a file so it is not overwritten? (y/n) ")
    if save == 'y':
        #rename the text file to the user's input
        new_name = input("Enter a new name for the text file: ")
        with open(new_name + '.txt', 'w',encoding="utf-8") as f:
            for i in text:
                f.write(i.get_text())
        # rename the table file to the user's input
        new_name = input("Enter a new name for the table file: ")
        tables = soup.find_all('tr')
        with open(new_name + '.txt', 'w',encoding="utf-8") as f:
            for i in tables:
                f.write(i.get_text())
        print("Saved to text.txt")
        print("To open this file run ./" + new_name + '.txt')
        break
    elif save == 'n':
        print("You can read the file \"text.txt\" and \"table.txt\" (This will be overwritten if you run this program again)")
        break
    else:
        print("Invalid input")
