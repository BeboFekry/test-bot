import streamlit as st
st.image("images/background.png")
st.title("I CARE")
st.info("Easy Healthcare for Anyone Anytime")
st.write("""You can access a three main modules:

Module 1: An AI based smart chatbot called "Caroline" talking to the patient 
and taking its disease symptoms, then diagnosing the disease and 
recommend making some tests as x-ray, MRI ... in addition, given 
information about the predicted disease as an overview, symptoms, and 
treatments. 
It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...) 

Module 2: A sequence of AI Computer Vision models for scanning medical 
imaging and tests it can scan (X-ray, MRI, CT, OCT, ECG, or Food image), 
detect the image type (Image Recognition), if it is medical imaging image, 
applying anatomical recognition, disease evaluation, disease diagnosis. It 
can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, 
Breast Cancer, ...) 
It also can recognize 101 food types from images and shows the approximate number of calories per gram.

Module 3: An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.
""")
