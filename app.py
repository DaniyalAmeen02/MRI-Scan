import numpy as np
import streamlit as st
from PIL import Image  # If you're dealing with image files

st.title("MRI Scan Analysis")

# Upload file
uploaded_file = st.file_uploader("Choose an MRI scan file", type=["jpg", "png", "jpeg", "dcm"])

if uploaded_file is not None:
    # Read the file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # Example for handling images:
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded MRI Scan", use_column_width=True)

    # Further processing here...
else:
    st.warning("Please upload an MRI scan file.")
