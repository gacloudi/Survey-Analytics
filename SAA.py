import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
import datetime
conn = sqlite3.connect('response.db', check_same_thread=False)
c = conn.cursor()


q="SELECT * FROM response" 
c.execute(q)
data = c.fetchall()
#st.write(data)
clean_db = pd.DataFrame(data,columns=["NPS","Star", "Feature","Completion"])
a=len(clean_db[clean_db['NPS']>=8])
b=len(clean_db[clean_db['NPS']<=5])
c1=len(clean_db[(clean_db['NPS']>=6)])-a
x1=clean_db['NPS'].sum()
x2=clean_db['Feature'].value_counts()
x3=clean_db['Star'].value_counts()
st.write(x1,x2,x3,a,b,c1)
st.write(clean_db)
data_as_csv= clean_db.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download", 
    data_as_csv, 
    "benchmark-tools.csv",
    "text/csv",
    key="download-tools-csv",
)