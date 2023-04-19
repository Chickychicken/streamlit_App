import streamlit as st

st.title('Title of my application')

st.markdown('this is **bold text')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
    st.markdown('This is markdown **text**')

st.sidebar.title('title of sidebar')
st.sidebar.markdown('Markdown **text** in the *sidebar*')

agree_sidebar = st.sidebar.checkbox('side bar check')

if agree_sidebar:
    st.sidebar.write('sidebar checked')