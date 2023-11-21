import streamlit as st
from os import listdir
import logging
import random
from flask import Response, Flask
import prometheus_client

logging.basicConfig(level=logging.DEBUG)

if not hasattr(st, "already_started_server"):
    st.already_started_server = True
    st.write("Due to some streamlit limitations, close this tab and open a new one")

    app = Flask(__name__)

    @app.route("/metrics/")
    def metrics():
        return Response(prometheus_client.generate_latest(), mimetype="text/plain; version=0.0.4; charset=utf-8")

    app.run(host="0.0.0.0", port=8888)


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
