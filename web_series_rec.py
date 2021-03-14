# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:05:22 2021

@author: NIKHIL NARASIMHA
"""

import ast
import pandas as pd

import time

import psycopg2

df = pd.read_csv("cleaned_data.csv")

rank_df = pd.read_csv("ranking.csv")

def web_series_rec(name, approach):
    if approach == 1:
        rec_seires = df[df["wb_name_edited"] == name]["rec_series"].to_list()
        rec_seires = ast.literal_eval(rec_seires[0])
        rec_seires = pd.DataFrame(rec_seires, columns = ["wb_name_edited"])
        rec_seires = pd.merge(rec_seires,df.loc[df["wb_name_edited"].isin(rec_seires["wb_name_edited"])], on = "wb_name_edited" ) 
        rec_seires = rec_seires.drop_duplicates(subset='wb_name_edited')
        rec_seires = rec_seires.fillna("Unknown")
        rec_seires = rec_seires.reset_index()
        return rec_seires
    elif approach ==2:
        rank1 = rank_df.sort_values(by=[name])
        rec_seires = rank1["wb_name"][0:31].to_list()
        rec_seires = pd.DataFrame(rec_seires, columns = ["wb_name"])
        rec_seires = pd.merge(rec_seires,df.loc[df["wb_name"].isin(rec_seires["wb_name"])], on = "wb_name" ) 
        rec_seires = rec_seires.drop_duplicates(subset='wb_name')
        rec_seires = rec_seires.fillna("Unknown")
        rec_seires = rec_seires.reset_index()
        return rec_seires

def recorder(query_given,web_liked):
    try:
        localtime = time.asctime( time.localtime(time.time()))
        conn = psycopg2.connect(database = "d4p1j3ph7ovdpj", user = "ncanedrmvoiwrt",
                            password = "b57d5188229f2a87e436a3185fb69631b1c0d479ce8df57a16d64a4c1d101213", host = "ec2-23-20-205-19.compute-1.amazonaws.com", port = "5432",connect_timeout=5)
        mycursor = conn.cursor()
    
        sql = "INSERT INTO record_webrec (query_name,result_name, time)VALUES (%s, %s, %s)"
        val = (query_given,web_liked, localtime)
        mycursor.execute(sql, val)
        conn.commit()
        conn.close()
    except:
        print("recording Failed")
        pass
