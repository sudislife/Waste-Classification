import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

IMAGE_SIZE = 224
class_names = ['battery', 'biological', 'cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def preprocess_image(image):
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    image = np.array(image)
    image = image.reshape(1, IMAGE_SIZE, IMAGE_SIZE, 3)
    return image

def classify_waste(image, class_names):
    image = preprocess_image(image)
    model = tf.keras.models.load_model('models/MobileNetv2_model.h5')
    y_pred = model.predict(image)
    print(np.argmax(y_pred, axis=1))
    confidence = y_pred[0][np.argmax(y_pred, axis=1)]
    y_pred = class_names[np.argmax(y_pred, axis=1)[0]]
    return y_pred, confidence[0]

uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Classify the image
    label, confidence = classify_waste(image, class_names)
    st.write('Class: ', label)
    st.write('Confidence: ', confidence)
