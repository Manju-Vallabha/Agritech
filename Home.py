import streamlit as st
import json
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
st.set_page_config(layout='wide',page_title="Agri Tech", page_icon="🪵")
google_logo = load_lottiefile("Animation - 1711075172542.json")
gemini_logo = load_lottiefile("Animation - 1711075470161.json")
title = st.container()
content = st.container()
with title:
    
    text = 'Agri - Tech'
    title = f"""
        <div style='
            font-family: arial;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        '>{text}<h2>{"🌾 Cultivate a brighter future with AgriTech 🌾"}</h2><h2>{"AI Powered Smart Agriculture Assisstant"}</h2><br>
        </div>
        """
    st.markdown(title, unsafe_allow_html=True)
with content:
    c1,c2,c3 = st.columns([2,5,2])
    st.image("test1.jpg", use_column_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    title = "Welcome to AgriTech: Empowering Farmers with Data-Driven Solutions"
    text = "In the heartlands where fields stretch to the horizon and the rhythm of seasons dictates livelihoods, lies an age-old challenge: how to cultivate crops with efficiency, precision, and resilience. This challenge forms the bedrock of agriculture, an industry pivotal to sustenance and economies worldwide. Yet, in the face of evolving climate patterns, resource constraints, and growing demand, traditional farming methods often find themselves stretched to their limits.<br><br>Join us on a journey into the future of agriculture, where technology meets tradition, and data becomes the cornerstone of sustainable farming practices. Together, let's cultivate a brighter, more resilient future for farmers and communities worldwide with AgriTech."
    html_code = f"""
            <div style='
                background-color: #2A2937;
                border-radius: 5px;
                padding: 20px;
                font-family: Arial;
                font-size: 20px;
                border: 2px;
                '><h3>{title}</h3>
                <div style='
                    font-family: monospace;
                    font-size: 18px;
                '>
                {text}<br><br></div>
            </div>
            """

    st.markdown(html_code, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    c_1, c_2 = st.columns([4,2])
    # with c_1:
    #     title = "Technology in Agritech"
    #     #text = "At Agritech, we leverage the advanced capabilities of Google Cloud Vertex AI for our model training needs. With Vertex AI, we streamline the entire model training process, from data preparation to model deployment, ensuring efficiency and effectiveness at every step.<br><br>One of the key features we utilize within Vertex AI is AutoML, which allows us to rapidly prototype and deploy high-quality models with minimal manual intervention. Whether it's image recognition, natural language processing, tabular data analysis, or video understanding, AutoML enables us to train models quickly and efficiently, accelerating our development timelines."
    #     html_code = f"""
    #         <div style='
    #             background-color: #2A2937;
    #             border-radius: 5px;
    #             padding: 20px;
    #             font-family: Arial;
    #             font-size: 20px;
    #             border: 2px;
    #             '><h3>{title}</h3>
    #             <div style='
    #                 font-family: monospace;
    #                 font-size: 18px;
    #             '>
    #             {text}<br><br></div>
    #         </div>
    #         """
    #     st.markdown(html_code, unsafe_allow_html=True)
    #     with c_2:
    #         st_lottie(google_logo, speed=1, width=400, height=400)
    # st.markdown("<br><br>", unsafe_allow_html=True)
    c_11, c_22 = st.columns([2,4])
    with c_11:
        st_lottie(gemini_logo, speed=1, width=400, height=400)
    with c_22:
        title = "Chat with Gemini: Your Personal Farming Assistant"
        text = "Meet Gemini, your personal farming assistant powered by the latest advancements in natural language processing and machine learning. Gemini is designed to provide you with real-time insights, recommendations, and solutions to your farming queries, helping you make informed decisions and optimize your farming practices.<br><br>Whether you're looking for weather updates, crop recommendations, pest control strategies, or market insights, Gemini has you covered. Simply ask Gemini a question, and let the power of AI transform your farming experience."
        html_code = f"""
            <div style='
                background-color: #2A2937;
                border-radius: 5px;
                padding: 20px;
                font-family: Arial;
                font-size: 20px;
                border: 2px;
                '><h3>{title}</h3>
                <div style='
                    font-family: monospace;
                    font-size: 18px;
                '>
                {text}<br><br></div>
            </div>
            """
        st.markdown(html_code, unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    text = "The Project is developed by Team Raghava from Kalasalingam Academy of Research and Education, Krishnankoil, Tamil Nadu, India."
    html_code = f"""
            <div style='
                background-color: #2A2937;
                border-radius: 5px;
                padding: 20px;
                font-family: Arial;
                font-size: 20px;
                border: 2px;
                '><h3>{"Team Members"}</h3>
                <div style='
                    font-family: monospace;
                    font-size: 18px;
                '>
                {text}<br><br></div>
            </div>
            """
    st.markdown(html_code, unsafe_allow_html=True)
