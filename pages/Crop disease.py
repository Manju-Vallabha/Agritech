
import base64
import json
import streamlit as st
import os
from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from streamlit_lottie import st_lottie

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "growpro-413910-bf223dc2c423.json"
st.set_page_config(page_title="Crop Disease Detector", page_icon="🌿")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
logo = load_lottiefile('Animation - 1711069098118.json')
image = ''
def predict_image_classification_sample(
    project: str,
    endpoint_id: str,
    image_content,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

    with image_content as f:
        file_content = f.read()

    # The format of each instance should conform to the deployed model's prediction input schema.
    encoded_content = base64.b64encode(file_content).decode("utf-8")
    instance = predict.instance.ImageClassificationPredictionInstance(
        content=encoded_content,
    ).to_value()
    instances = [instance]

    # See gs://google-cloud-aiplatform/schema/predict/params/image_classification_1.0.0.yaml for the format of the parameters.
    parameters = predict.params.ImageClassificationPredictionParams(
        confidence_threshold=0.5,
        max_predictions=5,
    ).to_value()
    endpoint_path = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint_path, instances=instances, parameters=parameters
    )

    
    # See gs://google-cloud-aiplatform/schema/predict/prediction/image_classification_1.0.0.yaml for the format of the predictions.
    predictions = response.predictions
    for prediction in predictions:
        print(dict(prediction))
        pred = prediction['displayNames']
        
        return pred

with st.container():
    text = 'Rice Disease Detection'
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
predict_button = False
input_type = ''
co1,co2,co3 = st.columns([1,1,1])
with st.sidebar:
    st.title("Expreience the power of AI in Agriculture")
    st.info("This crop disease detection model is trained on Google Cloud AI Platform using the PlantVillage dataset. The model can predict three classes of rice diseases: Bacterial leaf blight, Brown spot, and Leaf smut.")
    input_type = st.selectbox("Pick one", ["<Select>","Upload Image","Camera Input", ])
    if input_type == "Upload Image":
        image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if input_type == "<Select>":
    with co2:
        st_lottie(logo, speed=1, width=200, height=200, key="initial")
    st.latex(r''' \text{ 👈 Select an input type to upload an image or use the camera to take a snapshot.}''')       
if input_type == "Camera Input":
    image = st.camera_input("Pick a snapshot")
if image and input_type == 'Upload Image' != None:
    st.image(image, caption='Uploaded Image', use_column_width=True)
if image != None and input_type != "<Select>":
    predict_button = st.button("Predict")
if predict_button and image is not None:
    # Convert the UploadedFile object to bytes
    r = predict_image_classification_sample(
    "546899236073",
    "2716121375071797248",
    image
)
    p = r[0]
    text = ''
    title = ''
    if p == 'Bacterial_leaf_blight':
        title = "Bacterial leaf blight"
        text = 'Bacterial leaf blight is a common disease in rice plants. It is caused by the bacteria Xanthomonas oryzae pv. oryzae. The symptoms of bacterial leaf blight include water-soaked lesions on the leaves, which later turn yellow and then brown. The lesions may also have a characteristic "blighting" effect, where the entire leaf withers and dies. Other symptoms may include wilting, stunting, and reduced yield. It is important to diagnose and manage bacterial leaf blight to prevent significant crop losses.'
        prevention = 'To prevent bacterial leaf blight, it is important to plant disease-resistant rice varieties, rotate crops, and practice good field hygiene. Infected plants should be removed and destroyed to prevent the spread of the disease. Copper-based bactericides can also be used to control the disease.'
        symptoms = 'Symptoms of bacterial leaf blight include water-soaked lesions on the leaves, which later turn yellow and then brown. The lesions may also have a characteristic "blighting" effect, where the entire leaf withers and dies. Other symptoms may include wilting, stunting, and reduced yield.'
    elif p == 'Brown_spot':
        title = "Brown spot"
        text = 'Brown spot is a common fungal disease in rice plants. It is caused by the fungus Cochliobolus miyabeanus. The symptoms of brown spot include small, circular to oval lesions on the leaves that are initially water-soaked and later turn brown. The lesions may have a yellow halo around them. As the disease progresses, the lesions may coalesce, leading to large necrotic areas on the leaves. Other symptoms may include wilting, stunting, and reduced yield. It is important to diagnose and manage brown spot to prevent significant crop losses.'
        prevention = 'To prevent brown spot, it is important to plant disease-resistant rice varieties, rotate crops, and practice good field hygiene. Infected plants should be removed and destroyed to prevent the spread of the disease. Fungicides can also be used to control the disease.'
        symptoms = 'Symptoms of brown spot include small, circular to oval lesions on the leaves that are initially water-soaked and later turn brown. The lesions may have a yellow halo around them. As the disease progresses, the lesions may coalesce, leading to large necrotic areas on the leaves. Other symptoms may include wilting, stunting, and reduced yield.'
    
    elif p == 'Leaf_smut':
        title = "Leaf smut"
        text = 'Leaf smut is a common fungal disease in rice plants. It is caused by the fungus Tilletia barclayana. The symptoms of leaf smut include elongated, spindle-shaped galls on the leaves that are initially green and later turn black. The galls may be covered with a powdery mass of spores. Other symptoms may include wilting, stunting, and reduced yield. It is important to diagnose and manage leaf smut to prevent significant crop losses.'
        prevention = 'To prevent leaf smut, it is important to plant disease-resistant rice varieties, rotate crops, and practice good field hygiene. Infected plants should be removed and destroyed to prevent the spread of the disease. Fungicides can also be used to control the disease.'
        symptoms = 'Symptoms of leaf smut include elongated, spindle-shaped galls on the leaves that are initially green and later turn black. The galls may be covered with a powdery mass of spores. Other symptoms may include wilting, stunting, and reduced yield.'
    st.success(f"Predicted Disease: {p}")
    html_code = f"""
            <div style='
                background-color: #2A2937;
                border-radius: 5px;
                padding: 20px;
                font-family: Arial;
                font-size: 20px;
                border: 2px;
                '>
                <h4>{title}</h4>
                <div style='
                    font-family: monospace;
                    font-size: 18px;
                '>
                {text}<br><br><h3>{"Symptoms"}</h3>{symptoms}<br><br><h3>{'Preventions'}</h3>{prevention}<br></div>
            </div>
            """

    st.markdown(html_code, unsafe_allow_html=True)

# [END aiplatform_predict_image_classification_sample]
