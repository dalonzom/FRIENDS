from lxml import html
import requests
import pandas as pd
from openpyxl import load_workbook 
season1 = map(str, range(101, 125, 1))
season2 = map(str, range(201, 225, 1))
season3 = map(str, range(301, 326, 1))
season4 = map(str, range(401, 424, 1))
season5 = map(str, range(501, 524, 1))
season6 = map(str, range(601, 625, 1))
season7 = map(str, range(701, 725, 1))
season8 = map(str, range(801, 824, 1))
season9 = map(str, range(901, 923, 1))
season9 = season9 + ["0923-0924"]
season10 = map(str, range(1001, 1017, 1))
season10 = season10 + ["1017-1018"]

allSeasons = [season1, season2, season3, season4, season5, season6, season7, season8, season9, season10]

from lxml import etree
import requests
'''
s = "///Users/Marissa/Downloads/test.htm"
page = requests.get(s)
tree = etree.HTML(page.text)
element = tree.xpath('./body/font[2]/p[5]/b')
print(element)
content = etree.tostring(element[0])
print(content)
'''
#/html/body/font/p[3]
page = requests.get('https://fangj.github.io/friends/season/0212-0213.html')
tree = html.fromstring(page.content)
print(tree)
tempD = tree.xpath('/html/body/p[2]/font/text()')
print(tempD)
#/html/body/p[3]/text()
#/html/body/p[1]
count = 1
#page = requests.get('https://fangj.github.io/friends/season/0501.html')
#tree = html.fromstring(page.content)
#tempD = tree.xpath('/html/body/p['+str(2)+']/text()')
#print(tempD)

'''
writer = pd.ExcelWriter("data.xlsx")

for season in allSeasons:
   # print(season)
    dialouge = []
    speakers = []
    for episode in season:
        print(episode)
        if(count == 10):
            page = requests.get('https://fangj.github.io/friends/season/' + str(episode) + '.html')
        else:
            page = requests.get('https://fangj.github.io/friends/season/0' + str(episode) + '.html')
        tree = html.fromstring(page.content)


        i = 1
        while tree.xpath('/html/body/p['+str(i)+']/font/text()') != [] or tree.xpath('/html/body/font/p['+str(i)+']/text()') != [] or tree.xpath('/html/body/p['+str(i)+']/text()') != [] or tree.xpath('/html/body/p['+str(i+1)+']/text()') or tree.xpath('/html/body/p['+str(i+1)+']/font/text()') != [] or tree.xpath('/html/body/font/p['+str(i+1)+']/text()'):
            tempD = tree.xpath('/html/body/p['+str(i)+']/font/text()')
            if tempD == []:
                tempD = tree.xpath('/html/body/font/p['+str(i)+']/text()')
            if tempD == []:
                tempD = tree.xpath('/html/body/p['+str(i)+']/text()')
           # print(tempD)
            dialouge.append(''.join(tempD))
            tempS = tree.xpath('/html/body/p['+str(i)+']/font/b/text()')
            if tempS == []:
                tempS = tree.xpath('/html/body/p['+str(i)+']/b/text()')
            if tempS == []:
                tempS = tree.xpath('/html/body/font['+str(i)+']/p['+str(i)+']/b/text()')
            speakers.append(''.join(tempS))
            i = i+1

        episodes = pd.DataFrame({'dialogue' : dialouge, 'speaker' : speakers})


    name = 'Season'  + str(count)
   # print(episode)
    episodes.to_excel(writer, name)
    count = count+1
writer.save()

'''