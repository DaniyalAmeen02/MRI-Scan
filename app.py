import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf

st.title("MRI Scan Analysis")

# Upload file
uploaded_file = st.file_uploader("Choose an MRI scan file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read the file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # Example for handling images:
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded MRI Scan", use_column_width=True)

        # Preprocess the image
        img = image.resize((128, 128))  # Resize the image to the size expected by the model
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Normalize to [0, 1] range

        # Load the pre-trained model
        # Assuming the model is saved in the same directory as 'tumor_detection_model.h5'
        model = tf.keras.models.load_model('tumor_detection_model.h5')

        # Predict
        prediction = model.predict(img_array)

        # Determine if a tumor is detected
        if prediction[0][0] > 0.5:
            st.error("Tumor detected in the MRI scan.")
        else:
            st.success("No tumor detected in the MRI scan.")
else:
    st.warning("Please upload an MRI scan file.")
