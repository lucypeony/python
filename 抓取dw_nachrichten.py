myURL='https://www.dw.com/de/media-center/deutschkurse/s-100816?filter=&type=17&programs=17269854&sort=date&results=36'

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
#import seaborn as sns  #what is it : a library for making statistical graphics. built on top of matplotlib and closely integrated with pandas 
#%matplotlib inline 

#from urllib.requests import urlopen #to open urls 
import requests
from bs4 import BeautifulSoup # to extract data from html files 

html=requests.get(myURL)
html=html.content
soup = BeautifulSoup(html,'html.parser')

all_links = soup.find_all('a')
for link in all_links:
    print(link.get('href'))
    
