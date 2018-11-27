import pandas as pd 
import numpy as np 
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML


characters = pd.read_excel("word_frequency.xlsx", sheet_name="Characters")

characters = characters[(characters["Characters"] != "mnca") & (characters["Characters"] != "mon") & (characters["Characters"] != "richard") & (characters["Characters"] != "burke")]
print(characters.iloc[6:17,:])
seasons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
names = ["Janice", "Gunther", "Ben", "Carol", "Susan", "Kathy", "Julie", "Emily", "Richard"]
#Initialize and set up figure 
init_notebook_mode(connected=True)

figure = {
    'data': [],
    'layout': {},
    'frames': []
}
#Set up the layout of the graph axis and slider
figure['layout']['xaxis'] = { 'title': 'Character'}
figure['layout']['yaxis'] = {'range': [0, 175], 'title': 'Lines'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    'args': [
        'transition', {
            'duration': 400,
            'easing': 'linear'
        }
    ],
    'initialValue': '1',
    'plotlycommand': 'update',
    'values': seasons,
    'visible': True,
}
#Set up layout of the Play and Pause Buttons 
figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'linear'}}],
                'label': 'Play',
                'method': 'animate',
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate', 
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': True,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]
#Set inital values for the slider 
sliders_dict = {
    'active': 1,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Season:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

#Read data into the figure. We just want the x column names, so we put 
# nothing important in the Y axis 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

data_dict = { 
    'x' : names, 
    'y' : a, 
    'mode': 'markers',
        
}
figure['data'].append(data_dict)
count = 1 
for season in seasons: 
    frame = {'data': [], 'name':  str(season)}
   
    data_dict = {
 
        'x' : names, 
        'y' : characters.iloc[6:17,count], 
        'mode': 'markers',
        'marker': {
            'size' : 30 
        }
   }

    count = count + 1
    frame['data'].append(data_dict)
    figure['frames'].append(frame)
    
    #Set up so the slider moves as the data updates
    slider_step = {'args': [
        [season],
        {'frame': {'duration': 0, 'redraw': False},
        'mode': 'immediate',
        'transition': {'duration': 0}}
       
        
    ],
    'label': season,
    'method': 'animate'}
    sliders_dict['steps'].append(slider_step)
  


figure['layout']['sliders'] = [sliders_dict]

plotly.offline.plot(figure, filename='minorCharacterLines.html')


overallGraph = go.Bar(
    y = tuple(characters.iloc[6:17,11].values.tolist()),
    x = [ "Janice", "Gunther", "Ben", "Carol", "Susan", "Kathy", "Julie", "Emily", "Richard"]
)
layout = go.Layout(
    title = 'Overall Lines', 
    xaxis = dict(
        title='Character', 
    ),
    yaxis = dict(
        title= 'Lines'
    ), 
    legend=dict(orientation="h")
)

data = [overallGraph]
fig = go.Figure(data=data,layout=layout)
#Plot in html
plotly.offline.plot(fig, filename='minorOverallLines.html')

