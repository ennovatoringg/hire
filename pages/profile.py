import streamlit as st
import pandas as pd
st.title("your profile")

uploaded_file = st.file_uploader("Choose a file")

picture = st.camera_input("Take a picture")


if picture:
    with open ('test.jpg','wb') as file:
          file.write(picture.getbuffer())

