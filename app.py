import streamlit as st 
from os import listdir

image_names= listdir("images/")
image_paths = ["images/"+ image for image in image_names]

st.set_page_config(page_title="Generative Art With Go")

st.title("Generative Art with Go!")
st.markdown("A gallery to display images generated using Golang by Pavan Gudiwada. Code [here](https://github.com/pavangudiwada/generative-art-with-go)")
st.image(image=image_paths)
