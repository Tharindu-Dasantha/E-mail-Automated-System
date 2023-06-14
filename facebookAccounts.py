from bs4 import BeautifulSoup
import requests
import re
import time

def open_scraper(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    
    divbox = soup.find(class_="merchant__useful_section merchant__useful_section__social")
    lilist = divbox.find("li", class_="mlr__submenu__item mlr__submenu__itemnotprint mlr__submenu__item__social")
    a_button = lilist.find("a").get("href")
    link = "https://www.yellowpages.ca/" + a_button
    
    return link

filename = input("Enter the filename with the txt: ")
filenameToRead = "Website/Facebook/" + filename
filenameToWrite = "Website/Facebook/" + "output_" + filename
openfile = open(filenameToRead)
openfileToWrite = open(filenameToWrite, 'w')
lines = set(openfile.readlines())
amount = str(len(lines))

# open_scraper("https://www.yellowpages.ca/bus/Ontario/North-York/Charloo-s-West-Indian-Foods-Inc/8165198.html?what=shop&where=Toronto+ON&useContext=true")
count = 1
for line in lines:
    if re.match("https://", line):
        print("Scraping", str(count)+'/'+amount, line)
        link = open_scraper(line)
        openfileToWrite.write(f"{link}\n")
    else:
        print("not a line. " + f"{count}/{amount}")
        continue
    count += 1
    
    