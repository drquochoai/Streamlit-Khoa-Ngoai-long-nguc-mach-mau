import streamlit as st
import numpy as np

# add a title
st.title('My First Streamlit App')

# navigate to a _1_Trang_Chủ.py page
# Navigate to _1_Trang_Chủ.py
if st.button("Go to Home Page"):
    # Requires Streamlit 1.16.0 or newer
    st.switch_page("pages/Trang_Chu.py")
# add a file input to the sidebar