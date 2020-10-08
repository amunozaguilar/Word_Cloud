# -*- coding: utf-8 -*-
"""
@author: Alex
"""

# Import all libraries
import re
import wikipedia
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# Load data from Wikipedia
wiki = wikipedia.page('Chile')
text = wiki.content
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')

# Define a function for execute library and rescale images
def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud) 
    plt.axis("off");

# Load a image
mask = np.array(Image.open('.../upvote.png'))

# Setting for view of image
wordcloud = WordCloud(width = 3000, height = 2000, 
                      random_state=1, background_color='black', 
                      colormap='rainbow', collocations=False, 
                      stopwords = STOPWORDS, mask=mask).generate(text)

plot_cloud(wordcloud)
