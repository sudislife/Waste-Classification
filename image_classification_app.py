import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

IMAGE_SIZE = 224
BATCH_SIZE = 8
class_names = ['battery', 'biological', 'cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def preprocess_image(image):
    image = np.array(image)
    image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
    image = image / 255.0
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

st.title("Waste Classification App")

uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Classify the image
    label, confidence = classify_waste(image, class_names)
    
    label = 'Class: ' + label
    st.write(label)
    confidence = 'Confidence: ' + str(round(confidence*100, 2)) + '%'
    st.write(confidence)

    if 'battery' in label:
        st.write('Batteries are NOT to be thrown in any of the bins. They can cause fires at landfills. So, please drop them off for free at Drysdale or Geelong Resource Recovery Centres')
        st.write('Alternatively, ALDI, IGA, Bunnings and Woolworths stores accept batteries for recycling')
    
    elif 'biological' in label:
        st.write('Biological Waste is to be thrown in the Red Lid Rubbish Bin')
    
    elif 'cardboard' in label:
        st.write('Cardboard is to be thrown in the Yellow Lid Recycling Bin')
    
    elif 'glass' in label:            
        st.write('Glass is to be thrown in the Red Lid Recycling Bin')
    
    elif 'metal' in label:            
        st.write('Steel cans should be rinsed and placed in your yellow-topped recycling bin')
        st.write("Aluminium Cans and Foils can also be placed in the yellow topped recycling bin. Please rinse and squash them first")
    
    elif 'paper' in label:            
        st.write("Baking paper must be placed in the red landfill bin.")
        st.write("Envelopes, Magazines, and Newspapers can be placed in your yellow lid recycling bin. This include window faced envelopes.")
    
    elif 'plastic' in label:
        st.write("Plastic bags should be placed in the red landfill bin.")
        st.write("Remove the plastic bottle tops and place the empty plastic bottles in the Red recycling bin.")
    
    elif 'trash' in label:
        st.write("Trash is to be thrown in the Red Lid Rubbish Bin")

    
    st.write('Misclassified? Click one of the buttons below.')

    if st.button('Battery'):
        st.write('Batteries are NOT to be thrown in any of the bins. They can cause fires at landfills. So, please drop them off for free at Drysdale or Geelong Resource Recovery Centres')
        st.write('Alternatively, ALDI, IGA, Bunnings and Woolworths stores accept batteries for recycling')

    if st.button('Biological'):
        st.write('Biological Waste is to be thrown in the Red Lid Rubbish Bin')

    if st.button('Cardboard'):
        st.write('Cardboard is to be thrown in the Yellow Lid Recycling Bin')

    if st.button('Glass'):
        st.write('Glass is to be thrown in the Red Lid Recycling Bin')

    if st.button('Metal'):
        st.write('Steel cans should be rinsed and placed in your yellow-topped recycling bin')
        st.write("Aluminium Cans and Foils can also be placed in the yellow topped recycling bin. Please rinse and squash them first")

    if st.button('Paper'):
        st.write("Baking paper must be placed in the red landfill bin.")
        st.write("Envelopes, Magazines, and Newspapers can be placed in your yellow lid recycling bin. This include window faced envelopes.")

    if st.button('Plastic'):
        st.write("Plastic bags should be placed in the red landfill bin.")
        st.write("Remove the plastic bottle tops and place the empty plastic bottles in the Red recycling bin.")

    if st.button('Trash'):
        st.write("Trash is to be thrown in the Red Lid Rubbish Bin")
