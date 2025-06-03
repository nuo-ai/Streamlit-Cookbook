import streamlit as st

if 'my_key'  not in st.session_state:
    st.session_state['my_key']="value"
    
if 'my_list' not in st.session_state:
    st.session_state.my_list = []

st.text_input("Your name", key="name")
st.slider('Select a number',key='number')
'''Session state content:'''
st.write(st.session_state)
