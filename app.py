import streamlit as st

st.title("NeuroScan: Brain Tumor Detection")
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Load the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # Predict
    prediction = predict_image(img, model)
    
    # Display
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("Prediction: ", prediction)
