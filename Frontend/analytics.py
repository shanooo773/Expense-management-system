
import streamlit as st
from datetime import datetime
import requests
import pandas as pd
from streamlit import columns
import altair as alt
Api_url='http://127.0.0.1:8000'

def analytics():
    col1,col2=columns(2)
    with col1:
        start_date=st.date_input('Start Date',datetime(2024,8,2))
    with col2:
        end_date = st.date_input('End Date', datetime(2024, 8, 15))

    if st.button('Get Analytics'):
        data={
            'start_date':start_date.strftime('%Y-%m-%d'),
            'end_date':end_date.strftime('%Y-%m-%d')
        }
        ans=requests.post(f'{Api_url}/analytics',json=data)
        ans=ans.json()
        data=[]
        for key,val in ans.items():
            data.append({
               'category':key,
                'total':val['total'],
                'percentage':val['percentage']
            })
        df=pd.DataFrame(data)
        df=df.sort_values(by="percentage",ascending=False)




        col3,col4=columns(2)
        with col3:
            st.bar_chart(data=df.set_index('category')['percentage'],width=0,height=0,use_container_width=True)

        df['total'] = df['total'].map("{:.2f}".format)
        df['percentage']=df['percentage'].map("{:.2f}".format)
        with col4:
            base = alt.Chart(df).encode(x='category:N')

            bar = base.mark_bar(color='orange').encode(y='percentage:Q')
            line = base.mark_line(color='blue').encode(y='total:Q')

            st.altair_chart((bar + line).properties(
                width=600,
                height=400,
                title='Percentage and Total Expenses per Category'
            ), use_container_width=True)
        st.dataframe(df)


