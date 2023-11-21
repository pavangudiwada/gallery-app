import streamlit as st
from os import listdir
import logging
import random


logging.basicConfig(level=logging.DEBUG)

image_names = listdir("images/")
image_paths = ["images/" + image for image in image_names]
logging.debug("Imported Image Paths")

st.set_page_config(page_title="Generative Art With Go")

st.title("Generative Art with Go!")
st.markdown(
    "A gallery to display images generated using Golang by Pavan Gudiwada. Code [here](https://github.com/pavangudiwada/generative-art-with-go)"
)
logging.debug("Displaying Images")
num_images = st.slider("Number of Images displayed", min_value=2, max_value=len(image_paths), step=1)
random_images = st.toggle("Display Random images", value=True)
if random_images:
    random.shuffle(image_paths)
st.image(image=image_paths[:num_images])
