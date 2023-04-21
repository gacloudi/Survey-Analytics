import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
import datetime
from streamlit_star_rating import st_star_rating
st.header("Survey Analytics")
st.write("---")
c1,c2=st.columns(2)

conn = sqlite3.connect('response.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS response (NPS number,Star number, Feature Text,Completion Time)')

with c1:
    NPS=st.slider("1.How likely would you be to recommend our products to a friend or colleague?",1,10,1)
    g=st.write("Enter Your Ratings?")
    star=st_star_rating("",maxValue=5,defaultValue=3)
with c2:
    Feature=st.multiselect("2.Feature you like",['An','Bn','C'])
st.write("---")
#st.write(Feature)
#xf="".join(str(x) for x in Feature)
xf=','.join(Feature)
#st.write(type(xf))
sub=st.button("Submit")
if sub:
    ts=datetime.datetime.now()
    df=pd.DataFrame([[NPS,star,xf,ts]],columns=['NPS','Star','Feature','Completion'])
    df.to_sql('response',conn,if_exists='append',index=False)
    #SAA.main()
st.write(df)
# q="SELECT * FROM response" 
# c.execute(q)
# data = c.fetchall()
# #st.write(data)
# clean_db = pd.DataFrame(data,columns=["NPS", "Feature","Completion"])
# x1=clean_db['NPS'].sum()
# x2=clean_db['Feature'].value_counts()
# st.write(x1,x2)
    

