#Below Streamlit is used for web app.
import streamlit as st
#python imaging library Pillow
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

    # Create a file uploader component allowing the user to upload a file
    uploaded_image = st.file_uploader("Upload Image")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

# Check if the image exists meaning the user has uploaded a file
elif uploaded_image:
    # Open the user uploaded image with PIL
    img2 = Image.open(uploaded_image)

    # Convert the image to grayscale
    gray_camera_img2 = img2.convert('L')

    # Display the grayscale image on the webpage
    st.image(gray_camera_img2)

    #program streamlit run C:\enter path here\PycharmProjects\pythonProject1\ColortoGrayScaleConvertor.py
