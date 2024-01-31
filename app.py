import streamlit as st
from PIL import Image
import pandas as pd
import os
import numpy as np

# Function to load images from URLs
def load_image(url):
    img =  Image.open(url)
    print(img.size)


# Function to display images side by side
def display_images(images):
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(images[0])
    with col2:
        st.image(images[1])
    with col3:
        try:
        
            st.image(images[2])
        except:
            pass
    
# Function to navigate through images

# Load folder links from a separate file
folder_links = pd.read_csv('folder_links.csv')

# Sidebar: Folder selection
selected_folder_col1 = st.sidebar.selectbox('Select Folder for Column 1', folder_links['Folder'])
selected_folder_col2 = st.sidebar.selectbox('Select Folder for Column 2', folder_links['Folder'])
selected_folder_col3 = st.sidebar.selectbox('Select Folder for Column 3', folder_links['Folder'])

# Load images from the selected folders
url1 = folder_links.loc[folder_links['Folder'] == selected_folder_col1].iloc[0,1]
selected_images_col1 =[os.path.join(url1,im) for im in os.listdir(url1)]
url2 = folder_links.loc[folder_links['Folder'] == selected_folder_col2].iloc[0,1]
selected_images_col2 =[os.path.join(url2,im) for im in os.listdir(url2)]
url3 = folder_links.loc[folder_links['Folder'] == selected_folder_col3].iloc[0,1]
selected_images_col3 =[os.path.join(url3,im) for im in os.listdir(url3)]

# Main content
st.title('Image Viewer')
if 'index' not in st.session_state:
    st.session_state.index = 0

st.session_state.index = st.session_state.index % len(os.listdir(url1))

# Display images
display_images([selected_images_col1[st.session_state.index], selected_images_col2[st.session_state.index], selected_images_col3[st.session_state.index]])

col1, col2 = st.columns(2)
with col1:
    if st.button('Previous'):
        st.session_state.index -= 1

with col2:
    if st.button('Next'):
        st.session_state.index += 1

