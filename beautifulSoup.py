#Data Visualization Final Project
#HTML scraper gathering transcripts for all season except Season 2

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook 

#List all episodes
season1 = map(str, range(101, 125, 1))
season2 = map(str, range(201, 212, 1))
season2 = season2 + ["212-0213"] + map(str, range(214,225))
season3 = map(str, range(301, 326, 1))
season4 = map(str, range(401, 424, 1))
season5 = map(str, range(501, 524, 1))
season6 = map(str, range(601, 615, 1))
season6 = season6 + ["615-0616"] + map(str, range(617, 625))
season7 = map(str, range(701, 723, 1))
season8 = map(str, range(801, 824, 1))
season9 = map(str, range(901, 923, 1))
season9 = season9 + ["923-0924"]
season10 = map(str, range(1001, 1017, 1))
season10 = season10 + ["1017-1018"]

allSeasons = [season1, season2, season3, season4, season5, season6, season7, season8, season9, season10]


writer = pd.ExcelWriter("data.xlsx")
count = 1
#Loop through all seasons and all episodes
for season in allSeasons:
    text = []
    for episode in season:
        print(episode)
        print(count)
        #Link to transcripts
        if(count >= 10):
            quote_page = 'https://fangj.github.io/friends/season/' + str(episode) + '.html'
        else:
            quote_page = 'https://fangj.github.io/friends/season/0' + str(episode) + '.html'
        
        print(quote_page)

        #Open and parse
        page = urllib2.urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        i = 1
        #Find all paragraphs, clean, and store in array
        while i < len(soup.find_all("p")):
            name_box = soup.find_all("p")[i]
            name = name_box.text.strip()
            text.append(name)
            i = i+1
            
    #Convert to dataframe, write to excel
    episodes = pd.DataFrame({"text": text})
    test = 'Season'  + str(count)
         
    episodes.to_excel(writer, test)
    count = count+1
    writer.save()

