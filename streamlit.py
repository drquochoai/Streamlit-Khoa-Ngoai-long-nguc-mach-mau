import streamlit as st
import numpy as np

# add a title
st.title('My First Streamlit App')

# add side bar with beautiful menu design
st.sidebar.title('Menu')
st.sidebar.subheader('Choose a page to navigate')
page = st.sidebar.radio('Go to', ['Home', 'About', 'Contact'])
if page == 'Home':
    st.title('Home Page')
    st.write('Welcome to the Home Page')
elif page == 'About':
    st.title('About Page')
    st.write('Welcome to the About Page')
else:
    st.title('Contact Page')
    st.write('Welcome to the Contact Page')
# add a file input to the sidebar