import numpy as np
import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import json

from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="Soil Testing AI",
    page_icon=":bar_chart:",
    layout="wide"

)
text = 'Soil Nutrient Prediction using AI'
title = f"""
        <div style='
            font-family: arial;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        '>{text}<br><br>
        </div>
        """
st.markdown(title, unsafe_allow_html=True)
co1,co2,co3 = st.columns([1,1,1])
coo1,coo2,coo3 = st.columns([1,1,1])
data = pd.read_csv('info.csv')

predicted_pH = 0
chemical = ""
nutrients = ""
crops = ""



# Load the model
model = joblib.load('model_xgb.pkl')
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
logo = load_lottiefile('soil.json')

def calculate_average_rgb(image):
    # Convert the image to RGB
    img = image.convert('RGB')
    
    # Get the color data
    data = img.getdata()
    
    # Initialize variables to store total values
    r_total = 0
    g_total = 0
    b_total = 0
    
    # Calculate total of each component
    for r, g, b in data:
        r_total += r
        g_total += g
        b_total += b
    
    # Calculate averages
    num_pixels = len(data)
    avg_r = r_total / num_pixels
    avg_g = g_total / num_pixels
    avg_b = b_total / num_pixels
    
    return int(avg_r), int(avg_g), int(avg_b)

def predict_pH(red, green, blue):
    # Create a dataframe with the input values
    input_data = pd.DataFrame({'blue': [int(blue)], 'green': [int(green)], 'red': [int(red)]})
    
    # Use the loaded model to make predictions
    prediction = model.predict(input_data)
    
    return prediction[0]


with co2:
    st_lottie(logo, speed=1, width=400, height=400, key="initial")

with st.sidebar:
     st.title("Expreience the power of AI in Agriculture")
     st.info("The Power of AI in agriculture is immense. This AI model can predict the pH value of the soil by analyzing the RGB values of the soil image. Upload an image of the soil to get started.")
     #st.success("The model uses an XGBoost algorithm to predict the pH value based on the RGB values of the soil image.")
     input_type = st.selectbox("Pick one", ["Upload Image","Camera Input", ])
     if input_type == "Upload Image":
          uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if input_type == "Camera Input":
     uploaded_file = st.camera_input("Choose an image...")
if input_type == "Upload Image" or input_type == "Camera Input":
     if uploaded_file is not None:
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
     else:
            st.warning("Please upload an image to get started.")
if st.button("Test the soil") and uploaded_file is not None :
        image = Image.open(uploaded_file)
        # Calculate the average RGB values
        average_rgb = calculate_average_rgb(image)
        # Display the average RGB values
        predicted_pH = predict_pH(average_rgb[0], average_rgb[1], average_rgb[2])
        if int(predicted_pH) < 4:
             chemical = data['Chemical Characteristics'][0]
             nutrients = data['Deficient Nutrients'][0]
             crops = data['Suitable Crops'][0]
        elif int(predicted_pH) >= 4 and int(predicted_pH) < 6:
                chemical = data['Chemical Characteristics'][1]
                nutrients = data['Deficient Nutrients'][1]
                crops = data['Suitable Crops'][1]
        elif int(predicted_pH) == 6:
                chemical = data['Chemical Characteristics'][2]
                nutrients = data['Deficient Nutrients'][2]
                crops = data['Suitable Crops'][2]
        elif int(predicted_pH) == 7:
                chemical = data['Chemical Characteristics'][3]
                nutrients = data['Deficient Nutrients'][3]
                crops = data['Suitable Crops'][3]
        elif int(predicted_pH) == 8:
                chemical = data['Chemical Characteristics'][4]
                nutrients = data['Deficient Nutrients'][4]
                crops = data['Suitable Crops'][4]
        elif int(predicted_pH) >= 9:
                chemical = data['Chemical Characteristics'][5]
                nutrients = data['Deficient Nutrients'][5]
                crops = data['Suitable Crops'][5]

        info = f"The Ph of the Soil is {int(predicted_pH)}.\n\nChemical Characteristics: {chemical} .\n\nNutrients: {nutrients} ."
        st.success(info)
        if int(predicted_pH) <= 4 and int(predicted_pH) >= 8:
            st.info("The crops can be grown in the soil are: "+crops)
        else:
            st.warning("The soil is not suitable for any crops.")
        
