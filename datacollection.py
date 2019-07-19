#Importing pandas to view the data and save as csv
import pandas as pd

#Importing requests and BeautifulSoup for web scraping
import requests
from bs4 import BeautifulSoup

#Importing csv to store files
import csv

#Getting the baseurl 
try:
    page=requests.get("https://karki23.github.io/Weather-Data/assignment.html")
except:
    print("Error not found")
    exit()

#Initializing the BS object and getting body of the html
soup=BeautifulSoup(page.content,"html.parser")
html=list(soup.children)[2]
body=list(html.children)[3]
 
 #Creating a list of all the urls
baseurl="https://karki23.github.io/Weather-Data/"
urls=[(baseurl+href['href']) for href in soup.find_all('a',href=True)]

#Scraping the data from the url and saving to csv
for i in range(0,50):
    url=urls[i]
    city=url.split("/")[-1].split(".")[0]
    try:
        page=requests.get(url)
    except:
        print("Error not found")
        exit()
    soup=BeautifulSoup(page.content,"html.parser")
    table=soup.find('table')
    data=pd.read_html(str(table),header=0)[0]
    data.to_csv("Insert path here"+city+".csv")
    print(city+" data from "+url +" saved as CSV.")

print("Data scraping complete.")