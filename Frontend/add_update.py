
import streamlit as st
from datetime import datetime
import requests


Api_url=' http://127.0.0.1:8000'

def add_update():
    result_dte = st.date_input('Enter Date', datetime(2024, 8, 2))
    result_data = requests.get(f'{Api_url}/expenses/{result_dte}')

    if result_data.status_code == 200:
        result = result_data.json()

    else:
        st.error('Bad request')

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key='expenseForm'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader('Amount')
        with col2:
            st.subheader('Category')
        with col3:
            st.subheader("Notes")

        response = []
        for i in range(0, 5):
            if i < len(result):
                amount = result[i]['amount']
                category = result[i]['category']
                notes = result[i]['notes']
            else:
                amount = 0.0
                category = "Rent"
                notes = 'None'
            with col1:
                amount_input = st.number_input(label='amount', min_value=0.0, value=amount, step=1.0, key=f"amount_{i}",
                                               label_visibility='collapsed')
            with col2:
                category_input = st.selectbox(label='category', options=categories, index=categories.index(category),
                                              key=f'category_{i}', label_visibility='collapsed')
            with col3:
                note_input = st.text_input(label='notes', value=notes, key=f'notes_{i}', label_visibility='collapsed')
            response.append({
                'amount': amount_input,
                'category': category_input,
                'notes': note_input
            })
        submit_res = st.form_submit_button()
        if submit_res:
            filter_response = [resp for resp in response if resp['amount'] > 0]
            ans = requests.post(f'{Api_url}/expenses/{result_dte}', json=filter_response)
            if ans.status_code == 200:
                st.write('Expense added successfully')