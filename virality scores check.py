# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:29:08 2020

@author: Satyam Jaiswal

"""
#imports
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
import numpy as np


import nltk
nltk.download('punkt') #if you don't have punkt

#url load for The Times of India
url = 'https://timesofindia.indiatimes.com/world'
page = requests.get(url)

#start beautifulsoup
soup = BeautifulSoup(page.content,'html5lib')
headline = soup.findAll('a',attrs={'class':'w_img'})
news = []

for i in headline:    
    if not i['href'].startswith('http'):
        news.append('https://timesofindia.indiatimes.com/world'+i['href'])
        df=[]
        

for j in news:
    try:
        article=Article(j,language='en')
        article.download()
        article.parse()
        article.nlp()
        data={}
        data['title']=article.title # get titles of respective news article
        data['keywords']=article.keywords #get their respective keywords
        df.append(data)
    except:
        continue
    
# url load for India Today
        
url_1 = 'https://www.indiatoday.in/'
page_1 = requests.get(url_1)

#start beautifulsoup

soup_1 = BeautifulSoup(page_1.content,'html.parser')

main=soup_1.find_all('main',attrs={'class':'container'})

division=main[0].find_all('div',attrs={'class':'col-sm-4 col-md-4 col-lg-4 padrht0 mrgb30 home-top-story'})

ul = division[0].find_all('ul',attrs={'class':'itg-listing'})    
 
lists = ul[0].find_all('li') 
news_1=[]
for i in lists:
    content = i.find_all('a')
    for j in content:
        news_1.append('https://www.indiatoday.in/'+j['href'])
    
for k in news_1:
    
        article_1 = Article(k,language='en')
        article_1.download()
        article_1.parse()
        article_1.nlp()
        data={}
        data['title'] = article_1.title
        data['keywords'] = article_1.keywords
        df.append(data)
                
    #create data frame
    
dframe = pd.DataFrame(df)   
full_list=[] 
for each in dframe['keywords']:
    full_list = full_list + each
    
element,count=np.unique(full_list,return_counts=True)
element,count=list(element),list(count)
Dict={}
for i in range(len(element)):
    Dict[element[i]] = count[i]
scores=[]
for k in range(len(list(dframe['keywords']))):
    score=0
    for l in list(dframe['keywords'])[k]:
        score = score + Dict[l]
        
    scores.append(score)
    
dframe['scores'] = scores # add scores column to data frame

#appling min max scaling

dframe['scores'] = (dframe['scores']-min(list(dframe['scores'])))/(max(list(dframe['scores']))-min(list(dframe['scores'])))

dframe.to_csv('file_1.csv') # export the data file
    
    

    

    

    
