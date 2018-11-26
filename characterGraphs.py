import pandas as pd 
import numpy as np 
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML


characters = pd.read_excel("word_frequency.xlsx", sheet_name="Characters")

characters = characters[(characters["Characters"] != "mnca") & (characters["Characters"] != "mon") & (characters["Characters"] != "richard") & (characters["Characters"] != "burke")]
seasons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
names = ["Rachel", "Monica", "Phoebe", "Chandler", "Ross", "Joey"]
#Initialize and set up figure 
init_notebook_mode(connected=True)

figure = {
    'data': [],
    'layout': {},
    'frames': []
}
#Set up the layout of the graph axis and slider
figure['layout']['xaxis'] = { 'title': 'Lines'}
figure['layout']['yaxis'] = {'range': [0, 1200], 'title': 'Lines'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    'args': [
        'transition', {
            'duration': 400,
            'easing': 'linear'
        }
    ],
    'initialValue': '0',
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
    'transition': {'duration': 300, 'easing': 'circle-in'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

#Read data into the figure. We just want the x column names, so we put 
# nothing important in the Y axis 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data_dict = { 
    'x' : characters.iloc[0:6, 0], 
    'y' : a, 
    'mode': 'markers',
        
}
figure['data'].append(data_dict)
count = 0 
for season in seasons: 
    frame = {'data': [], 'name': "Season " + season}
    data_dict = {
    #go.Bar( 
        'x' : names, 
        'y' : characters.iloc[0:6,count], 
        'mode': 'markers',
        'marker': {
            'size' : 10 
        }
        
   # )
   }
    count = count + 1
    frame['data'].append(data_dict)
    figure['frames'].append(frame)
    
    #Set up so the slider moves as the data updates
    slider_step = {'args': [
        [season],
        {'frame': {'duration': 300, 'redraw': False},
        'mode': 'immediate',
        'transition': {'duration': 300}}
       
        
    ],
    'label': season,
    'method': 'animate'}
    sliders_dict['steps'].append(slider_step)
    print(slider_step)

    
figure['layout']['sliders'] = [sliders_dict]
#print(sliders_dict)
plotly.offline.plot(figure, filename='characterLines.html')

'''''
overallGraph = go.Bar(
    y = tuple(characters.iloc[0:6,11].values.tolist()),
    x = ["Rachel", "Monica", "Phoebe", "Chandler", "Ross", "Joey"]
   # type = 'scatter', 
   # mode = "markers"
)
layout = go.Layout(
    title = 'Lines Per Season', 
    xaxis = dict(
        title='Friend', 
    ),
    yaxis = dict(
        title= 'Lines'
    ), 
    legend=dict(orientation="h")
)

data = [overallGraph]
fig = go.Figure(data=data,layout=layout)
#Plot in html
plotly.offline.plot(fig, filename='overallLines.html')

minorCharacters = go.Scatter(
    
    x = tuple(characters.iloc[7:17,11].values.tolist()),
    mode = markers
)
layout = go.Layout(
    title = "Minor Character Overall Lines",
    xaxis = dict(
        title = "Character", 
    ),
    yaxis = dict(
        title = "Lines"
    ),
    legend=dict(orientation="h")
)
fig = go.Figure(data=minorCharacters,layout=layout)
plotly.offline.plot(fig, filename="minorOverall.html")
'''
