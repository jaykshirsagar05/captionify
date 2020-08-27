import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image
import io

st.title('Caption Generator')

# fastapi endpoint
url = 'http://fastapi:8000'
endpoint = '/segmentation'
endpoint1 = '/caption'

st.write('''Generate brief caption of the selected image.
         This streamlit example uses a FastAPI service as backend.
         Visit this URL at `:8000/docs` for FastAPI documentation.''')  # description and instructions

image = st.file_uploader('insert image')  # image upload widget


def process(image, server_url: str):

    m = MultipartEncoder(
        fields={'file': ('filename', image, 'image/jpeg')}
        )

    r = requests.post(server_url,
                      data=m,
                      headers={'Content-Type': m.content_type},
                      timeout=8000)

    return r

def process1(image, server_url: str):
    m = MultipartEncoder(
        fields={'file': ('filename', image, 'image/jpeg')}
        )
    r = requests.post(server_url,data=m,headers={'Content-Type': m.content_type},
                      timeout=800000)

    return r


if st.button('Get segmentation'):

    if image is None:
        st.write("Insert an image!")  # handle case with no image
    else:
        segments = process(image, url+endpoint)
        segmented_image = Image.open(io.BytesIO(segments.content)).convert('RGB')
        st.image([image, segmented_image], width=300)  # output dyptich

if st.button('Get caption'):

    if image is None:
        st.write("Insert an image!")  # handle case with no image
    else:
        segments = process1(image, url+endpoint1)
        # segmented_image = Image.open(io.BytesIO(segments.content)).convert('RGB')
        st.image([image], width=300)  # output dyptich
        st.write(segments)
