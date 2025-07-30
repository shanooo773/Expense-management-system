import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

Api_url = 'http://127.0.0.1:8000'

def get_by_month():
    if st.button('Get Analytics By Month'):
        ans = requests.get(f'{Api_url}/yearmonth')
        ans = ans.json()

        df = pd.DataFrame(ans)
        df["total_expense"] = df["total_expense"].astype(float)

        df['month_dt'] = pd.to_datetime(df['month'], format='%B %Y')
        df = df.sort_values('month_dt')

        col3, col4 = st.columns(2)

        with col3:
            st.bar_chart(
                data=df.set_index('month')['total_expense'],
                use_container_width=True
            )

        with col4:
            line = alt.Chart(df).mark_line(point=True).encode(
                x=alt.X('month_dt:T', title='Month'),
                y=alt.Y('total_expense:Q', title='Total Expense')
            ).properties(
                width=600,
                height=400,
                title='Monthly Total Expenses'
            )
            st.altair_chart(line, use_container_width=True)


        df = df.drop(columns='month_dt')

        df["total_expense"] = df["total_expense"].map("{:.2f}".format)
        st.dataframe(df)
