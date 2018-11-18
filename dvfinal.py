#Chandler=1 Joey=2 Monica=3 Phoebe=4 Rachel=5 Ross=6

import pandas as pd
import collections
import matplotlib.pyplot as plt
import networkx as graph
import holoviews as hv
import matplotlib.image as mpimg

from matplotlib.cbook import get_sample_data

chandler = plt.imread('chandler.png')
joey = plt.imread('joey.png')
monica = plt.imread('monica.png')
phoebe = plt.imread('phoebe.png')
rachel = plt.imread('rachel.png')
ross = plt.imread('ross.png')
photos = [chandler, joey, monica, phoebe, rachel, ross]

#get number of plotlines per season for each character 
char2seasons =	{
  "Chandler": [],
  "Joey": [],
  "Monica": [],
  "Phoebe": [],
  "Rachel": [],
  "Ross": []
}
df = pd.read_csv('friendsdata.csv')
plotlines_per_seasons =collections.Counter(df['epseason'])

def get_plotlines_10seasons_per_character(season_number):
    a = [0,0,0,0,0,0]
    for i in range(0,plotlines_per_seasons[season_number]):
        if '1' in str(df['dynamics'][i]):
            a[0] = a[0] + 1
        if '2' in str(df['dynamics'][i]):
            a[1] = a[1] + 1
        if '3' in str(df['dynamics'][i]):
            a[2] = a[2] + 1
        if '4' in str(df['dynamics'][i]):
            a[3] = a[3] + 1
        if '5' in str(df['dynamics'][i]):
            a[4] = a[4] + 1
        if '6' in str(df['dynamics'][i]):
            a[5] = a[5] + 1
    char2seasons['Chandler'].append(a[0])
    char2seasons['Joey'].append(a[1])
    char2seasons['Monica'].append(a[2])
    char2seasons['Phoebe'].append(a[3])
    char2seasons['Rachel'].append(a[4])
    char2seasons['Ross'].append(a[5])


for i in range(1,11):
    get_plotlines_10seasons_per_character(i)

#get number of plotlines of each character per season
seasons2char =	{ 
        "season1": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season2": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season3": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season4": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season5": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season6": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season7": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season8": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season9": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
        "season10": { "Chandler": 0,"Joey": 0, "Monica": 0,"Phoebe": 0, "Rachel": 0,"Ross": 0},
    }

for i in range(0,10):
    seasons2char['season' + str(i+1)]['Chandler'] = char2seasons['Chandler'][i]
    seasons2char['season' + str(i+1)]['Joey'] = char2seasons['Joey'][i]
    seasons2char['season' + str(i+1)]['Monica'] = char2seasons['Monica'][i]
    seasons2char['season' + str(i+1)]['Phoebe'] = char2seasons['Phoebe'][i]
    seasons2char['season' + str(i+1)]['Rachel'] = char2seasons['Rachel'][i]
    seasons2char['season' + str(i+1)]['Ross'] = char2seasons['Ross'][i]
    
    
#get weights for networks based on relationships for twn seasons
r_data = {"rel_season1": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season2": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season3": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season4": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season5": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season6": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season7": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season8": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season9": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0},
          "rel_season10": {"12":0,"13":0,"14":0,"15":0,"16":0,"23":0,"24":0,"25":0,"26":0,"34":0,"35":0,"36":0,"45":0,"46":0,"56":0}}
          

def get_relationship_weights_per_season(season_number):
    index = df.index[df['epseason'] == season_number][0]
    for i in range(0,plotlines_per_seasons[season_number]):
        if df['dynamics'][i] > 6:
            chars = [int(d) for d in str(df['dynamics'][i + index])]
            for j in range(0,len(chars)-1):
                r_data['rel_season'+ str(season_number)][str(chars[j]) + str(chars[j + 1])] = r_data['rel_season'+ str(season_number)][str(chars[j]) + str(chars[j + 1])] + 1
            if df['dynamics'][i + index] > 99:
                r_data['rel_season'+ str(season_number)][str(chars[0]) + str(chars[len(chars)-1])] = r_data['rel_season'+ str(season_number)][str(chars[0]) + str(chars[len(chars)-1])] + 1
                
                
for i in range(1,11):
    get_relationship_weights_per_season(i)

#create weights for one season

 
def relationship_graph_for_season(season_number):
 #   fig = plt.figure()
    G = graph.Graph() 
    node_list = ['Chandler','Joey','Monica','Phoebe','Rachel','Ross']
    count = 0 
    for node in node_list:
        G.add_node(node,image=photos[count],size=.2)
        count = count+1


 
    pos=graph.circular_layout(G) 
    graph.draw_networkx_nodes(G,pos,node_color='blue',node_size=7500)
 
    labels = {}
    for node_name in node_list:
        labels[str(node_name)] =str(node_name)
    graph.draw_networkx_labels(G,pos,labels,font_size=16)
   
    for i in range(0, len(r_data['rel_season'+ str(season_number)])):
        vertices = [int(d) for d in str(r_data['rel_season'+ str(season_number)].keys()[i])]
        w = r_data['rel_season'+ str(season_number)].values()[i]
        G.add_edge(node_list[vertices[0] - 1],node_list[vertices[1] - 1],weight=w) 

        all_weights = []
 
    for (node1,node2,data) in G.edges(data=True):
        all_weights.append(data['weight']) 
 
    unique_weights = list(set(all_weights))


    for weight in unique_weights:
        weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['weight']==weight]
        width = weight*len(node_list)*3.0/sum(all_weights)
        graph.draw_networkx_edges(G,pos,edgelist=weighted_edges,width=width)
    
    plt.axis('off')
    plt.title('Relationships between characters in Season ' + str(season_number), y= 1.08)
    
    ax=plt.gca()
    fig=plt.gcf()
    label_pos = 0.5 # middle of edge, halfway between nodes
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    imsizes = graph.get_node_attributes(G, "size")
    images = graph.get_node_attributes(G, "image")
    i = 0
    for (node) in node_list:
        (x,y) = pos[node]
        xx,yy = trans((x,y)) # figure coordinates
        xa,ya = trans2((xx,yy)) # axes coordinates
  
        image = images[node]
        imsize = imsizes[node]
        a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
        a.imshow(photos[i])
        i = i+1
        a.set_aspect('equal')
        a.axis('off')
 
    #Plot the graph

    plt.show() 
    #plt.savefig("FRIENDS_SEASON" + str(season_number) + ".png")

for i in range(1,11):
    relationship_graph_for_season(i)





