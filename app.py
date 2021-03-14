# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:49:03 2021

@author: NIKHIL NARASIMHA
"""

#packages 
import streamlit as st

import random

import time

import pandas as pd

from PIL import Image

import QA

from mailbot import emailbot

from web_series_rec import web_series_rec , recorder



def ranking(a):
    stopwords = ["on", "tv", "ranked", "based", "in", "&", "high", "adventure", "video","" ]
    a = a.lower()
    a = a.replace("#","")
    a = [a for a in a.split() if a not in stopwords]
    return a

#df = pd.read_csv("cleaned_data.csv")
#page name and image
img = Image.open('bs.png')
st.set_page_config(page_title="Web Series Rec",page_icon=img,initial_sidebar_state="collapsed")

#Background Image
page_bg_img = '''
<style>
body {
background-image: url("https://www.creativity103.com/collections/Graphic/starboarder.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


#Title
title_html = """<div><p style="text-align:center; color:SeaGreen ; font-size:45px"><b><a style= "color:OrangeRed ;">Web</a><a style="color:SeaShell;"> Series </a> Recommdation</b></p></div>"""
st.markdown(title_html, unsafe_allow_html = True)

#Search Box

liked_series = st.text_input("")
button_clicked = st.button("Recommend")

#boder colour
color = ["LightSkyBlue","SandyBrown", "LightSalmon", "SteelBlue"]
color = random.choice(color)



#Html for name card
end_html = '''<h3 align="right">Nikhil Narasimha</h3> 
              <h3 align="right">7799528666</h3>'''


html = '''
        <div class="container" style="display: flex; border:2px solid {colour}; background-color: white;">
        <div style="width: 40%;" >
                <div>
                    <div style="width: 2%; ">
                        <img src={img} alt="Girl in a jacket" width="200" height="250">
                    </div>
                </div>
         </div>
         <br>
         <div style="flex-grow: 1; ">
                <div >
                       <h1  margin: 0px 0px 5px; style="font-family:verdana">{movie_name}</h1>
                       <div >
                            <span><b>Genre :</b></span> <a style="color:#000;">{genre}</a>
                       </div>
                        <div >
                             <span><b><img src=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATwAAACfCAMAAABTJJXAAAAAulBMVEX2xwAAAAD3zCf8zAD////+zgD/zgDhtgDeswCNcgCXegAoIABoVAB7ZAD6ygD0xgBsWAANCgDAmwDpvQBNPgDUrAAfGAD1wwCnhwBJOwDGoACcfgDNpgCSdgCzkQBxWwAWEgBENwC4lQBbSgAsJAA8MQCtjAD/1AD76K/878X634j++en989OEagAkHQAbFQAyKQD52XL412b//fX64pP756n+99/3z0D401VcSwARDgA+MgD53ID3zjG9vSkoAAAIjUlEQVR4nO2deV/iPBDHW0MKupCqgEVAULzXVdE91HWf9/+2HnoCIZMpPUzpZ377z2oHOvmaJtMcE6uR6O5lzyIhcl/vfibErPg/vzzPtGO7Ic97+bkO794idKnleXer8H4Ruq3kvSzhfSd2W8p7jeH9JnZby/sewvtD7DLIuw/gvZn2Yzfl+vDuqeJlkvd7AY8qXka5DeuBKl5GeT+sO4KXUd4v659pH3ZX7xY1eZnlLv6RSCQSiUQikUgkEolEIpFIpOIkmFrCtGOrYhxRNmPguuM4nAcMhJ6CGJ4dqHQ2+UJ6XUjRWCq7+WhrdbniLBvpbdsf3ciSXyqvHx5Op53Hs9HgZjZudS3ucKgmsTNbrbZTKq9ViXPAB7sVes32IQPJ0Be/wIybkTHHDAOdXD5OWoKr+LED4DOHXwePfUOY4PCOl2VjT5jxdvACnU+HjG06Xg94o2XJPJREBngLPY8sGV9N4E0Tb0UTxZAN3kITLjleD3inS3hDlEFmePaltdb01QSenRSK3aC22eHZV91VenWB102+DLfNAc++Wp2Jrgu8cVwjnEPUNg88+3KFS13g3cQ9Ib9GbXPBswfLXqMu8PYTeEeobT54yxaiNvDacX3o4qXPCa+TVL26wLuOSiRaeOlzwrOTPqMu8I6i7xLHeOHzwkva17rAi1siNsBN88JLOtzawItiFf6Im+aFZyeO1wXeLHyWeBs3xeGdXlyl+YLawDuL4IHftVl2GB7nzGrBdXhYN3jRuIqDW6aA5/engs+gyxNWM3hRrJIizEsJzx+mBy6P6gbvKCiQ6OOWqeGBPfd+3eCFsQoDH7UVpYUHDg3G7xj1gdf3bdkohWVqeFA1btcOXtCK804Ky9TwoBH9OErG4QnGHWG5rmsJh2/OIFUGXhCrOFAbv6q08MDe5zRlzWO8edPpPQe/Oj/tTLrKCcwqwAtiFY7OO9pbwHOBy9ep4DExmEu/7x0Xjq8YeHO/RCyFYX548zTw+ER15bpfcHNYDDybp5p3tAuAd4XDEx4YJHIFAuPwmgt441SGeeF9QzuM2ya4hMTeL5ReQfDGIs28o10AvCcsSJ5qn4BJkd1uQfBuGFyaNeWGd4LB68H1zldXAcEwvMVLkzNNY5gb3jM2qoJoWmCnURC8RdzPe2u/OVePyuWGd54TXuKBQXgn6z8uAgixHuZdrbOUXc8M72/seFZ4B8W1elnhfUg/O3JpL0uCF882ZYZ3WlyHmxWePNTblOcdH6sKzzYPTx5uG3NpDGlUWXjF9beZ4UnLUgZcwnlsEB7QWcUumIcnBSaPt5Jd/1TtefnwzvuCucML8AbFdbeZ4Ukr+S9vpeVlrtr7L4A3C4ZV4BVbLfPwpHGL+e26s0fOhfJzXwAPmQQJh73NwpOHycXz2o/z2wvl58qHdxTeAZ6OGpuHJ4/0Sr62jcG7iEIRcCJ0aBzeSC699JTsG4PXi15eBXSDCsC7lYa5pchkYAzeRzzgB92gCvD0i7eHwDa08uElc5PQDY7Nw+P60ZameXh/AYMqwFPOsSRyjcE7jOE9AwYVgOdopyyumGPqDSOe9GYngIF5eAOuXRPVcwieBh6zoDbFV4cTPB087XafET22WnjaCZ9jQfB08MAMCb76BE8LT+jWMroWwdPC062i5QRPCw8snh2MbBA8LTw4JYv/ikTwtPC4Go+vM0bw9PA0scoNwUPgaSb/xoLg6eFpYpUmwcPgwbEKswieHh4cqzxzgofBY1AyC38ageDp4Tnq5Sjh/jCCh8CD9ksNqM3DH1top57vHsHTwwNTgbQIHg4PSkLjLx8sCx66JnlH4EEFPPLdB3qT3Lse0dXwuwIPIBAstckJD6zV6D6MXYEH7LCdFlDzwJ1sT2l3eld40nug2dsdbl3OCQ/qjPBdj9VfqxLAA1ZfzgqABy7sRPfb7sBCnwAeUD2CpZc54YF5qdCd3h8YPPNLzEJ46lY92OiQFx40pR4nFgbhxRkcwGGLCiyrZbCDbn548LZxNDVItDIU/oYKLOgO4HFVjxa2StnhCSEc7xO6jCalmYcb8+DRxgpsJQhcVMYq4brW7PDc5rEmQwuaDinKeQ1nC6/AJpaw5qma9f18NQ8RmogrugW8a78Ce8+CMigDiqhSlgQvDjRgeGf+H0+AadDsTQhm4CljlTAUKAteH4VnD1zuDqGBWvukAltGQ3iqLq1VKrw412/mLaOrOdKNwlPGKmHxSoI3R1P9YnqsSs2znM2drU+iTHgdNNUvpgIzq+SFt9ks93iZ8JJ3q13ObhHBU8QqnTLhnSQNVlZ41wUmRMoJTxGrRIFYOfCWz1xWeEXmQ8oJTxHHz0ps8z6XPSUIT5/Fb14gu7zwFFMN/RLhrZwCBMKbaJOsF/diWwC8zVglevspA15/pdqA8Jpcs8dhVokUcDE8Z2PczSkL3nV39ZED4XFNgn/58DTT8OS8SJ+8JHij9ZSfEDx/9glKjj6uSNrLGN7G5XYp8K5GbsoT94LTRlhX/psudOgWne83Nzw5VonH2zKvGNjQU3vU3zwpkw0uegp9hvl6BO9LO9Hb/WIf2eAu4IFRETwx6Sg0jSN90ZqqL7AD5eeS822nqstLhWfcDvvNruDqM26Zo1RSMMcdHrTDt8fTzsx1iuxmY/UhxcMXQnkCcuKKfDm5oD5kObkvdgRzdLpyniKLwIWFg04JCabDO0Aq53YkEolEIpFIJBKJRCKRSJWXi5uQIO2ZdmCX9W7agd3VnvXdM+3DzurVuid4GeX9thoEL6O8B6vxQvSy6a1hNf4QvEzy7hfwqOpl03vDh9cw7cZOynsI4dGDu70WD20Ir0Hhyrby7hoxvMYPi/Bto6DexfAaP1+JXmp5bw+NVXiLyvfueQQQl+e93cfMEniL2nf37/2/PZJG/73/u3tYEvsfZO/stFWhe88AAAAASUVORK5CYII= alt="Girl in a jacket" width="50" height="25"></b></span>
                             <span><b><img src=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxMyI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJhIiB4MT0iMjkuMTkyJSIgeDI9Ijc1LjQyNiUiIHkxPSIwJSIgeTI9IjEwMCUiPjxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGOUVFQUMiLz48c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNEQkE1MDYiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48cGF0aCBmaWxsPSJ1cmwoI2EpIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik01OTIgNDI5LjVsLTQuMTE0IDIuMTYzLjc4NS00LjU4MS0zLjMyOC0zLjI0NSA0LjYtLjY2OUw1OTIgNDE5bDIuMDU3IDQuMTY4IDQuNi42NjktMy4zMjggMy4yNDUuNzg1IDQuNTgxeiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTU4NSAtNDE5KSIvPjwvc3ZnPg== alt="Girl in a jacket" width="20" height="20"></b></span> 
                             <span><a style="color:#000;">{rating} &nbsp; &nbsp; &nbsp; <span><b><img src = https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSGPrJDPg333JuyfVEH_77fjwl5AClF13OsQ&usqp=CAUalt="Girl in a jacket" width="20" height="25"></b> <a style="color:#000;">{ott}</span> </a></span>
                        </div>
                    <div>
                         <div > 
                             <span><a > <b>Seasons : </b> {seasons} &nbsp;  <b>Year : </b> {year}</a></span>                             
                        </div>
                        <div > 
                             <span><a > <b>Country : </b> {country} &nbsp; <b>Web Series Rank : </b> {ranking}</a></span>
                        </div>
                        <br>
                        <div>
                             <span style="font-size:10px" ><a><b style="color:SandyBrown" > {s1} </b> </a></span>
                        </div>
                    </div>
                </div>
        </div>
     </div>
    
     '''
    
print(f'start=',time.time())    
if len(liked_series) < 3:
    pass
elif (len(liked_series) >= 3 and button_clicked) or len(liked_series) >= 3:
    print(f'enter=',time.time())
    try:
        name, appracoh = QA.QA(liked_series)
        print(f'qa=',time.time())
        df = web_series_rec(name, appracoh)
        print(f'df=',time.time())
        search_word_html = """</style><div><p style="text-align:left; color:DarkGrey; font-size:30px; font-family: monospace;"><i>You have Searched for <b>"{series_liked_edited}"</b></i></p></div>"""
        search_word_html = search_word_html.format(series_liked_edited = name.title())
        st.markdown(search_word_html, unsafe_allow_html = True)
        html0 = html.format(img = df["logo"][0],movie_name = (df["wb_name"][0]).title(),genre = (df["genre_edited"][0][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][0]).title(),year = (df["lower_year"][0]).title(),ott = (df["ott_edited"][0]).title(),country = df["country_edited"][0].title(),rating = (df["Imdb_rating"][0]).title(),s1 = df["ranking_genre"][0].title(),ranking = df["ranking_overall_edited"][0], colour= color )
        st.markdown(html0, unsafe_allow_html=True)
        st.title(" ")
        html1 = html.format(img = df["logo"][1],movie_name = (df["wb_name"][1]).title(),genre = (df["genre_edited"][1][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][1]).title(),year = (df["lower_year"][1]).title(),ott = (df["ott_edited"][1]).title(),country = df["country_edited"][1].title(),rating = (df["Imdb_rating"][1]).title(),s1 = df["ranking_genre"][1].title(),ranking = df["ranking_overall_edited"][1], colour= color )
        st.markdown(html1, unsafe_allow_html=True)
        st.title(" ")
        html2 = html.format(img = df["logo"][2],movie_name = (df["wb_name"][2]).title(),genre = (df["genre_edited"][2][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][2]).title(),year = (df["lower_year"][2]).title(),ott = (df["ott_edited"][2]).title(),country = df["country_edited"][2].title(),rating = (df["Imdb_rating"][2]).title(),s1 = df["ranking_genre"][2].title(),ranking = df["ranking_overall_edited"][2], colour= color )
        st.markdown(html2, unsafe_allow_html=True)
        st.title(" ")
        html3 = html.format(img = df["logo"][3],movie_name = (df["wb_name"][3]).title(),genre = (df["genre_edited"][3][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][3]).title(),year = (df["lower_year"][3]).title(),ott = (df["ott_edited"][3]).title(),country = df["country_edited"][3].title(),rating = (df["Imdb_rating"][3]).title(),s1 = df["ranking_genre"][3].title(),ranking = df["ranking_overall_edited"][3], colour= color )
        st.markdown(html3, unsafe_allow_html=True)
        st.title(" ")
        html4 = html.format(img = df["logo"][4],movie_name = (df["wb_name"][4]).title(),genre = (df["genre_edited"][4][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][4]).title(),year = (df["lower_year"][4]).title(),ott = (df["ott_edited"][4]).title(),country = df["country_edited"][4].title(),rating = (df["Imdb_rating"][4]).title(),s1 = df["ranking_genre"][4].title(),ranking = df["ranking_overall_edited"][4], colour= color )
        st.markdown(html4, unsafe_allow_html=True)
        st.title(" ")
        html5 = html.format(img = df["logo"][5],movie_name = (df["wb_name"][5]).title(),genre = (df["genre_edited"][5][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][5]).title(),year = (df["lower_year"][5]).title(),ott = (df["ott_edited"][5]).title(),country = df["country_edited"][5].title(),rating = (df["Imdb_rating"][5]).title(),s1 = df["ranking_genre"][5].title(),ranking = df["ranking_overall_edited"][5], colour= color )
        st.markdown(html5, unsafe_allow_html=True)
        st.title(" ")
        html6 = html.format(img = df["logo"][6],movie_name = (df["wb_name"][6]).title(),genre = (df["genre_edited"][6][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][6]).title(),year = (df["lower_year"][6]).title(),ott = (df["ott_edited"][6]).title(),country = df["country_edited"][6].title(),rating = (df["Imdb_rating"][6]).title(),s1 = df["ranking_genre"][6].title(),ranking = df["ranking_overall_edited"][6], colour= color )
        st.markdown(html6, unsafe_allow_html=True)
        st.title(" ")
        html7 = html.format(img = df["logo"][7],movie_name = (df["wb_name"][7]).title(),genre = (df["genre_edited"][7][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][7]).title(),year = (df["lower_year"][7]).title(),ott = (df["ott_edited"][7]).title(),country = df["country_edited"][7].title(),rating = (df["Imdb_rating"][7]).title(),s1 = df["ranking_genre"][7].title(),ranking = df["ranking_overall_edited"][7], colour= color )
        st.markdown(html7, unsafe_allow_html=True)
        st.title(" ")
        html8 = html.format(img = df["logo"][8],movie_name = (df["wb_name"][8]).title(),genre = (df["genre_edited"][8][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][8]).title(),year = (df["lower_year"][8]).title(),ott = (df["ott_edited"][8]).title(),country = df["country_edited"][8].title(),rating = (df["Imdb_rating"][8]).title(),s1 = df["ranking_genre"][8].title(),ranking = df["ranking_overall_edited"][8], colour= color )
        st.markdown(html8, unsafe_allow_html=True)
        st.title(" ")
        html9 = html.format(img = df["logo"][9],movie_name = (df["wb_name"][9]).title(),genre = (df["genre_edited"][9][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][9]).title(),year = (df["lower_year"][9]).title(),ott = (df["ott_edited"][9]).title(),country = df["country_edited"][9].title(),rating = (df["Imdb_rating"][9]).title(),s1 = df["ranking_genre"][9].title(),ranking = df["ranking_overall_edited"][9], colour= color )
        st.markdown(html9, unsafe_allow_html=True)
        st.title(" ")
        html10 = html.format(img = df["logo"][10],movie_name = (df["wb_name"][10]).title(),genre = (df["genre_edited"][10][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][10]).title(),year = (df["lower_year"][10]).title(),ott = (df["ott_edited"][10]).title(),country = df["country_edited"][10].title(),rating = (df["Imdb_rating"][10]).title(),s1 = df["ranking_genre"][10].title(),ranking = df["ranking_overall_edited"][10], colour= color )
        st.markdown(html10, unsafe_allow_html=True)
        st.title(" ")
        html11 = html.format(img = df["logo"][11],movie_name = (df["wb_name"][11]).title(),genre = (df["genre_edited"][11][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][11]).title(),year = (df["lower_year"][11]).title(),ott = (df["ott_edited"][11]).title(),country = df["country_edited"][11].title(),rating = (df["Imdb_rating"][11]).title(),s1 = df["ranking_genre"][11].title(),ranking = df["ranking_overall_edited"][11], colour= color )
        st.markdown(html11, unsafe_allow_html=True)
        st.title(" ")
        html12 = html.format(img = df["logo"][12],movie_name = (df["wb_name"][12]).title(),genre = (df["genre_edited"][12][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][12]).title(),year = (df["lower_year"][12]).title(),ott = (df["ott_edited"][12]).title(),country = df["country_edited"][12].title(),rating = (df["Imdb_rating"][12]).title(),s1 = df["ranking_genre"][12].title(),ranking = df["ranking_overall_edited"][12], colour= color )
        st.markdown(html12, unsafe_allow_html=True)
        st.title(" ")
        html13 = html.format(img = df["logo"][13],movie_name = (df["wb_name"][13]).title(),genre = (df["genre_edited"][13][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][13]).title(),year = (df["lower_year"][13]).title(),ott = (df["ott_edited"][13]).title(),country = df["country_edited"][13].title(),rating = (df["Imdb_rating"][13]).title(),s1 = df["ranking_genre"][13].title(),ranking = df["ranking_overall_edited"][13], colour= color )
        st.markdown(html13, unsafe_allow_html=True)
        st.title(" ")
        html14 = html.format(img = df["logo"][14],movie_name = (df["wb_name"][14]).title(),genre = (df["genre_edited"][14][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][14]).title(),year = (df["lower_year"][14]).title(),ott = (df["ott_edited"][14]).title(),country = df["country_edited"][14].title(),rating = (df["Imdb_rating"][14]).title(),s1 = df["ranking_genre"][14].title(),ranking = df["ranking_overall_edited"][14], colour= color )
        st.markdown(html14, unsafe_allow_html=True)
        st.title(" ")
        html15 = html.format(img = df["logo"][15],movie_name = (df["wb_name"][15]).title(),genre = (df["genre_edited"][15][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][15]).title(),year = (df["lower_year"][15]).title(),ott = (df["ott_edited"][15]).title(),country = df["country_edited"][15].title(),rating = (df["Imdb_rating"][15]).title(),s1 = df["ranking_genre"][15].title(),ranking = df["ranking_overall_edited"][15], colour= color )
        st.markdown(html15, unsafe_allow_html=True)
        st.title(" ")
        html16 = html.format(img = df["logo"][16],movie_name = (df["wb_name"][16]).title(),genre = (df["genre_edited"][16][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][16]).title(),year = (df["lower_year"][16]).title(),ott = (df["ott_edited"][16]).title(),country = df["country_edited"][16].title(),rating = (df["Imdb_rating"][16]).title(),s1 = df["ranking_genre"][16].title(),ranking = df["ranking_overall_edited"][16], colour= color )
        st.markdown(html16, unsafe_allow_html=True)
        st.title(" ")
        html17 = html.format(img = df["logo"][17],movie_name = (df["wb_name"][17]).title(),genre = (df["genre_edited"][17][0:108].replace(" ",", ")).title(),seasons = (df["seasons"][17]).title(),year = (df["lower_year"][17]).title(),ott = (df["ott_edited"][17]).title(),country = df["country_edited"][17].title(),rating = (df["Imdb_rating"][17]).title(),s1 = df["ranking_genre"][17].title(),ranking = df["ranking_overall_edited"][17], colour= color )
        st.markdown(html17, unsafe_allow_html=True)
        st.title(" ")
        html18 = html.format(img = df["logo"][18],movie_name = (df["wb_name"][18]).title(),genre = (df["genre_edited"][18][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][18]).title(),year = (df["lower_year"][18]).title(),ott = (df["ott_edited"][18]).title(),country = df["country_edited"][18].title(),rating = (df["Imdb_rating"][18]).title(),s1 = df["ranking_genre"][18].title(),ranking = df["ranking_overall_edited"][18], colour= color )
        st.markdown(html18, unsafe_allow_html=True)
        st.title(" ")
        html19 = html.format(img = df["logo"][19],movie_name = (df["wb_name"][19]).title(),genre = (df["genre_edited"][19][0:42].replace(" ",", ")).title(),seasons = (df["seasons"][19]).title(),year = (df["lower_year"][19]).title(),ott = (df["ott_edited"][19]).title(),country = df["country_edited"][19].title(),rating = (df["Imdb_rating"][19]).title(),s1 = df["ranking_genre"][19].title(),ranking = df["ranking_overall_edited"][19], colour= color )
        st.markdown(html19, unsafe_allow_html=True)
        st.title(" ")
        print(f'data=',time.time())
        recorder(liked_series,name)
        #Email
        st.markdown("*You can drop your EmailID to get Top 25 Results for your Search throught Email.")
        col1, col2 = st.beta_columns(2)
        with col2:
            my_expander = st.beta_expander('Drop your Email here')
            mail_id = my_expander.text_input("  ")
            email_submit = my_expander.button('Get Mail!📧')
            if (r'@' in mail_id and len(mail_id) > 15)or (email_submit and r'@' in mail_id and len(mail_id) > 15) :
                result = emailbot(name,df,mail_id)
                #recorder_email(mail_id)
                my_expander.write(result)
        st.markdown(end_html, unsafe_allow_html=True)
    except:
        search_word_html = """</style><div><p style="text-align:left; color:DarkGrey; font-size:30px; font-family: monospace;"><i>No results for search</b></i></p></div>"""
        st.markdown(search_word_html, unsafe_allow_html = True)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
