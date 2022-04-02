TargetURL = 'https://www.vocabulary.com/lists/52473'

import requests
from bs4 import BeautifulSoup
import re


TargetHtml=requests.get(TargetURL).content
print(TargetHtml)

TargetSoup = BeautifulSoup(TargetHtml,'html.parser')

#get all the words and its meaning
'''
保存在三个lists里面：
word
definition 
example
最后输出到excel里面去
'''

words_tags = TargetSoup.find('li',{'class':'entry learnable'})
for this_word in words_tags :
    
