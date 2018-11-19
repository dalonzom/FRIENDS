
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook 
import numpy as np

season2 = map(str, range(201, 212, 1))
season2 = season2 + ["212-0213"] + map(str, range(214,225))





writer = pd.ExcelWriter("test.xlsx")
tempArray = []
for episode in season2: 
    quote_page = 'https://fangj.github.io/friends/season/0' + str(episode)+ '.html'
    print(quote_page)
    page = urllib2.urlopen(quote_page)
    text = []
    soup = BeautifulSoup(page, 'html.parser')
    i = 1

    while i < len(soup.find_all("p")):
        name_box = soup.find_all("p")[i]
        name = name_box.text.strip()
        text.append(name)
        i = i+1




    episodes = pd.DataFrame({"text": text})
    print(len(episodes))

    for i in range(0, len(episodes)):
        temp = episodes.iloc[i,:].str.split("\n", n=-1, expand=True)
        temp2 = temp.iloc[0,:].str.strip() 
        tempArray.append(temp2)

episodes = pd.concat(tempArray)


test = "testing"

episodes.to_excel(writer, test)
writer.save()
print("here")
