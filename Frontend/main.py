import streamlit as st
from add_update import add_update
from analytics import analytics
from get_by_month import get_by_month

tab1,tab2,tab3=st.tabs(['Add/Update','Analytics','Analytics by month'])

Api_url=' http://127.0.0.1:8000'
with tab1:
   add_update()
with tab2:
   analytics()
with tab3:
   get_by_month()
