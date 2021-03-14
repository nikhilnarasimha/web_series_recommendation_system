# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:05:38 2021

@author: NIKHIL NARASIMHA
"""
import pandas as pd

from fuzzywuzzy import process

from difflib import get_close_matches

df = pd.read_csv("cleaned_data.csv")

df.columns

web_series_list = df["wb_name_edited"].tolist()

rank = pd.read_csv("ranking_genre.csv")

rank = rank["name"].tolist()



def QA(web_series_name):
    approach_1 = 1
    approach_2 = 2
    ranking_list = [" best", "best ", "list", " top", "top "] 
    result = any(ele in web_series_name.lower() for ele in ranking_list)
    if result == True or len(web_series_name) > 35:
            stopwords = ["webseries", "series", "best", "top", "list" , "web"]
            name = web_series_name.lower()
            name = " ".join(a for a in name.split() if not a.isdigit())    
            name = " ".join(a for a in name.split() if a not in stopwords)
            genre = process.extract(name, rank)[0][0]
            return genre , approach_2
    else:
        try:
            name = get_close_matches(web_series_name, web_series_list,cutoff = 0.6)[0]
            return name , approach_1
        except:
            stopwords = ["webseries", "series", "best", "top", "list" , "web"]
            name = web_series_name.lower()
            name = " ".join(a for a in name.split() if not a.isdigit())    
            name = " ".join(a for a in name.split() if a not in stopwords)
            try:
                genre = get_close_matches(name, rank)[0]
                return genre , approach_2
            except:
                pass
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
