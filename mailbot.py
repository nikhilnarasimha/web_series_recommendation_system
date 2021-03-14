# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:39:04 2020

@author: NIKHIL NARASIMHA
"""
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

text = '''<html><h2 style= "color:black" >Hi {name}!</h2>
<br>
<h3 style= "color:black">Following are the similiar to {movie_name}</h3>
</html>'''
html = """
<html>
  <head></head>
  <body style= "color:DodgerBlue; font-size: 30px;">
    <p><b>1.%s</b></p>
    <p><b>2.%s</b></p>
    <p><b>3.%s</b></p>
    <p><b>4.%s</b></p>
    <p><b>5.%s</b></p>
    <p><b>6.%s</b></p>
    <p><b>7.%s</b></p>
    <p><b>8.%s</b></p>
    <p><b>9.%s</b></p>
    <p><b>10.%s</b></p>
    <p><b>11.%s</b></p>
    <p><b>12.%s</b></p>
    <p><b>13.%s</b></p>
    <p><b>14.%s</b></p>
    <p><b>15.%s</b></p>
    <p><b>16.%s</b></p>
    <p><b>17.%s</b></p>
    <p><b>18.%s</b></p>
    <p><b>19.%s</b></p>
    <p><b>20.%s</b></p>
    <p><b>21.%s</b></p>
    <p><b>22.%s</b></p>
    <p><b>23.%s</b></p>
    <p><b>24.%s</b></p>
    <p><b>25.%s</b></p>
    <br>
    <br>
    <br>
    <p style= "color:Black;">
    For Futher Information or a kind of communication can revert back. <br>
    <h4 style= "color:Black;">Thank You<h4>
    <h3 style="color:MediumSeaGreen" >Nikhil Narasimha</h3>
    <h3 style= "color:MediumSeaGreen"  >7799528666</h3>
    </p>
  </body>
</html>
"""

def fullname(email):
    mail = email.split("@")[0]
    name = re.sub("[^A-Za-z]"," ",mail)
    name.title()
    full_name = ""
    for i in name.split():
        if len(i) >= 4:
            nam = i.title()
        else:
            nam= i.upper()
        full_name += (" " + nam )
    return full_name.strip()

#recoder
def recorder_email(email):
    try:
        localtime = time.asctime( time.localtime(time.time()))
        conn = psycopg2.connect(database = "d4p1j3ph7ovdpj", user = "ncanedrmvoiwrt",
                            password = "b57d5188229f2a87e436a3185fb69631b1c0d479ce8df57a16d64a4c1d101213", host = "ec2-23-20-205-19.compute-1.amazonaws.com", port = "5432",connect_timeout=5)
        mycursor = conn.cursor()
    
        sql = "INSERT INTO record_email (email, time)VALUES (%s, %s)"
        val = (email, localtime)
        mycursor.execute(sql, val)
        conn.commit()
        conn.close()
    except:
        print("recording Failed")
        pass



def emailbot(movie_liked_edited,df,email):
    try:
        movies = df["wb_name_edited"][0:26].to_list()
        movies = [m.title() for m in movies]
        name = fullname(email)
        movies = df["wb_name_edited"][0:26].to_list()
        movies = [m.title() for m in movies]
        text = '''<html><h2 style= "color:black" >Hi {name}!</h2>
        <br>
        <h3 style= "color:black">Following are the Results for  <a style= "color:red ;font-size: 15px;">{movie_name}</a></h3>
        </html>'''
        html = """
        <html>
          <head></head>
          <body style= "color:DodgerBlue; font-size: 30px;">
            <p><b>1.%s</b></p>
            <p><b>2.%s</b></p>
            <p><b>3.%s</b></p>
            <p><b>4.%s</b></p>
            <p><b>5.%s</b></p>
            <p><b>6.%s</b></p>
            <p><b>7.%s</b></p>
            <p><b>8.%s</b></p>
            <p><b>9.%s</b></p>
            <p><b>10.%s</b></p>
            <p><b>11.%s</b></p>
            <p><b>12.%s</b></p>
            <p><b>13.%s</b></p>
            <p><b>14.%s</b></p>
            <p><b>15.%s</b></p>
            <p><b>16.%s</b></p>
            <p><b>17.%s</b></p>
            <p><b>18.%s</b></p>
            <p><b>19.%s</b></p>
            <p><b>20.%s</b></p>
            <p><b>21.%s</b></p>
            <p><b>22.%s</b></p>
            <p><b>23.%s</b></p>
            <p><b>24.%s</b></p>
            <p><b>25.%s</b></p>
            <br>
            <br>
            <br>
            <p style= "color:Black;">
            For Futher Information or a kind of communication can revert back. <br>
            <h4 style= "color:Black;">Thank You<h4>
            <h3 style="color:MediumSeaGreen" >Nikhil Narasimha</h3>
            <h3 style= "color:MediumSeaGreen"  >7799528666</h3>
            </p>
          </body>
        </html>
        """
        html1 = html %(movies[1],movies[2],movies[3],movies[4],movies[5],movies[6],movies[7],movies[8],movies[9],movies[10],movies[11],movies[12],movies[13],movies[14],movies[15],movies[16],movies[17],movies[18],movies[19],movies[20],movies[21],movies[22],movies[23],movies[24],movies[25])
        text = text.format(name = name,movie_name = movie_liked_edited.title())
        sender_address = 'ss.nikhilnarasimha@gmail.com'
        sender_pass = '7799528666'
        receiver_address = email
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Recommended Movies from MovRec Engine'
        message.attach(MIMEText(text, 'html'))
        message.attach(MIMEText(html1, 'html'))
        (df[["wb_name", "Imdb_rating_edited", "genre_edited", "ott_edited", "ranking_overall_edited"]]).to_csv("send.csv", index = False)
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("send.csv", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="send.csv"')
        message.attach(part)
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return "Mailed📧📧📧📭📫"
    except:
        return "Failed👎👎👎"















        




