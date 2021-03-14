# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:25:01 2021

@author: NIKHIL NARASIMHA
"""

#packages

import pandas as pd
import numpy as np

import re

from collections import OrderedDict

df = pd.read_csv("ULM.csv")

df.columns

#web seires name 

df["wb_name_edited"] = df.wb_name.apply(lambda x: x.lower())
df["wb_name_edited"] = df.wb_name_edited.apply(lambda x: x.strip())
df.wb_name[5]
df.wb_name_edited[5]

#web series imbd rating

df["Imdb_rating_edited"] = df.Imdb_rating.apply(lambda x: x.strip())
df["Imdb_rating_edited"] = df.Imdb_rating_edited.apply(lambda x: x.lower())
df.Imdb_rating[2]
df["Imdb_rating_edited"][2]

#web series genre
df["genre_edited"] = df["genre"].apply(lambda x: x.lower())
df["genre_edited"] = df["genre_edited"].apply(lambda x: x.replace("more",""))
df["genre_edited"] = df["genre_edited"].apply(lambda x: x.replace("genres",""))
df["genre_edited"] = df["genre_edited"].apply(lambda x: x.replace(","," "))
df["genre_edited"] = df["genre_edited"].apply(lambda x: x.strip())
df["genre_edited"] = df["genre_edited"].apply(lambda x: x.replace("&"," "))

df["genre"].to_csv("genre.csv")
def extra(word):
    w = word.split()
    aa = " ".join(w)
    return aa
df["genre_edited"] = df["genre_edited"].apply(lambda x: extra(x))

df["genre"][667]
df["genre_edited"][667]

#web series m-rating
df["m-rating"].value_counts()
df["m-rating"].unique()
df["m-rating_edited"] = df["m-rating"].apply(lambda x: x.replace("Rated:", ""))
df["m-rating_edited"] = df["m-rating_edited"].apply(lambda x: x.strip())

df["m-rating"][88]
df["m-rating_edited"][88]

#web series year
def lower_year(n):
    n = re.findall(r'\d+', n)
    n.sort()
    return n[:1].

df["lower_year"] = df["year"].apply(lambda x: lower_year(x))

lower_year(df["year"][99])
df["lower_year"][99]

#web series Seasons
df["seasons"].unique()

#web series ott
df["ott_edited"] = df["ott"].apply(lambda x: x.replace("On:", ""))
df["ott_edited"] = df["ott_edited"].apply(lambda x: x.replace(",", ""))
df["ott_edited"] = df["ott_edited"].apply(lambda x: x.replace("More Services", ""))
df["ott_edited"] = df["ott_edited"].apply(lambda x: x.replace("Free Services", ""))
df["ott_edited"] = df["ott_edited"].apply(lambda x: extra(x))

df["ott"][919]
df["ott_edited"][919]

#web series tags
df["tags_edited"] = df["tags"].apply(lambda x: x.replace("Tags:", ""))
df["tags_edited"] = df["tags_edited"].apply(lambda x: x.replace("," , " "))
df["tags_edited"] = df["tags_edited"].apply(lambda x: x.replace("." , ""))
df["tags_edited"] = df["tags_edited"].apply(lambda x: x.replace("More Tags" , ""))
df["tags_edited"] = df["tags_edited"].apply(lambda x: extra(x))
df["tags_edited"] = df["tags_edited"].apply(lambda x: remove_duplicates(x))
df["tags_edited"] = df["tags_edited"].apply(lambda x: x.lower())

df["tags"][99]
df["tags_edited"][17]

def remove_duplicates(word):
    a = word.split()
    aa = list(OrderedDict.fromkeys(a))
    aaa = " ".join(aa)
    return aaa

remove_duplicates(df["tags_edited"][99])

#web series country
df["country_edited"] = df["country"].apply(lambda x: x.replace("Country:", ""))
df["country_edited"] = df["country_edited"].apply(lambda x: x.replace(".", ""))
df["country_edited"] = df["country_edited"].apply(lambda x: x.replace("More Countries", ""))
df["country_edited"] = df["country_edited"].apply(lambda x: extra(x))
df["country_edited"] = df["country_edited"].apply(lambda x: x.lower())
df["country_edited"] = df["country_edited"].apply(lambda x: remove_duplicates(x))


df["country"][99]
df["country_edited"][3999]
df["country_edited"].sample(n= 15)
df["country_edited"].unique()

#web series cast
df["cast_edited"] = df["cast"].apply(lambda x: x.replace("[", ""))
df["cast_edited"] = df["cast_edited"].apply(lambda x: x.replace("]", ""))
df["cast_edited"] = df["cast_edited"].apply(lambda x: x.replace("'", ""))

def joinwords(text):
    text = text.replace(" ","")
    s = re.sub('([.,!?()])', r' \1 ', text)
    sen = re.sub('\s{2,}', ' ', s)
    return sen

joinwords(df["cast_edited"][5949])

df["cast_edited"] = df["cast_edited"].apply(lambda x: joinwords(x))
df["cast_edited"] = df["cast_edited"].apply(lambda x: x.lower())
df["cast_edited"] = df["cast_edited"].apply(lambda x: x.replace(",", ""))


df["cast_edited"].sample(n =15)

#web series ranking_overall
df["ranking_overall"][0]
df["ranking_overall_edited"] = df["ranking_overall"].apply(lambda x: x.replace(",", ""))
df["ranking_overall_edited"] = df["ranking_overall_edited"].apply(lambda x: re.findall(r'\d+', x))


df["ranking_overall_edited"].sample(n=13)

#web series ranking_genre
import re
s= df["ranking_genre"][9]
s = s.replace("Ranked in", "")
s = s.lower()
search_word = "tv on netflix"
res = re.search(r'(\d+)\s*{0}'.format(re.escape(search_word)), s)
if res:
    print(res.group(1))
df["ranking_genre"][9]

search = list(ranking.keys())

d = []

def ranker(s,name):
    ranking = start_dict()
    ranking["name"] = name
    s = s.replace("Ranked in", "")
    s = s.lower()
    for i in search:
        search_word = i
        res = re.search(r'(\d+)\s*{0}'.format(re.escape(search_word)), s)
        if res:
            ranking[search_word] = res.group(1)
    return ranking
    
ranker(df["ranking_genre"][9], df["wb_name"][9])

for s,n in zip(df["ranking_genre"],df["wb_name"]):
    rank = ranker(s,n)
    d.append(rank)

ranking = pd.DataFrame(d)
ranking.to_csv("ranking.csv")
ranking = ranking.replace(r'', np.NaN)

ranking["tv on netflix"] = ranking["tv on netflix"].astype(float)

a = ranking.sort_values("tv on netflix")

#web series description_rg (votes)
s = df["description_rg"][1]
def votes(s):
    s = s.replace(",","")
    res = re.search(r'(\d+)\s*{0}'.format(re.escape("votes")), s)
    if res:
        return res.group(1)
    else:
        return "None"

df["voters"] = df["description_rg"].apply(lambda x: votes(x))
df["description_rg"][9500]    
df["voters"][9500]

df.to_csv("cleaned_data.csv")


#web series description     

df["desc_edited"] = df["description"].apply(lambda x: keywordsexc_punc(x))
df["desc_edited2"] = df["description"].apply(lambda x: keywordsexc_punc(x))

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

from nltk.stem import PorterStemmer
ps =PorterStemmer()

def keywordsexc_punc(text):   
    import nltk
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens ]
    sen = ' '.join(words)
    import re
    s = re.sub('([.,!?()])', r' \1 ', sen)
    sen = re.sub('\s{2,}', ' ', s)
    tokens = word_tokenize(sen)
    words = [word for word in tokens if word.isalpha()]
    sen = ' '.join(words)
    tokens = word_tokenize(sen)
    words = [word for word in tokens if not word in stop_words]
    sen = ' '.join(words)   
    tokens = word_tokenize(sen)
    words = [ps.stem(word) for word in tokens ]
    sen = ' '.join(words)
    return sen

keywordsexc_punc(df["description"][1])
df["desc_edited"][1]

df["ULM"] = df["ULM"].apply(lambda x: x.replace(")","a"))
df["ULM"] = df["ULM"].apply(lambda x: re.sub(r'\ba\d+\d+\d+\d+a\b', '', x))
df["ULM"] = df["ULM"].apply(lambda x: re.sub(r"\s'", '', x))


df["ULM"][9]

df.to_csv("ULM.csv", index = False)

re.sub(r"\s'", '', x)
