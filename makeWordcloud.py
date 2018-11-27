import pandas as pd 
import numpy as np
from wordcloud import WordCloud 
from PIL import Image 

phrases = pd.read_excel("word_frequency.xlsx", sheet_name="Phrases")

phrases = phrases[(phrases["Phrases"] != "ramoray") & (phrases["Phrases"] != "remoray") & (phrases["Phrases"] != "remore") & (phrases["Phrases"] != "phalange")
    & (phrases["Phrases"] != "regina")]
test = pd.DataFrame()
test["Phrases"] = phrases["Phrases"]
test["Frequencies"] = phrases["Overall"] 
print(test)
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
# %matplotlib inline
import seaborn as sns
# Bokeh
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, CustomJS, ColumnDataSource, Slider
from bokeh.layouts import column
from bokeh.palettes import all_palettes
d = {}
for a, x in test.values:
    d[a] = x
plt.figure()
wordcloud = WordCloud(background_color="white")
wordcloud.generate_from_frequencies(frequencies=d)
plt.imshow(wordcloud, interpolation="bilinear")
#plt.imshow(WordCloud(background_color="white").generate(str(phrases["Phrases"])))  
plt.axis("off")

plt.ioff()
wordcloud.to_file("wordcloud.png")
plt.show()