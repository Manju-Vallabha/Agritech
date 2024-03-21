import base64
import streamlit as st
import os

from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "growpro-413910-bf223dc2c423.json"

def predict_image_classification_sample(
    image_content,
    project: str = "546899236073",
    endpoint_id: str = "2716121375071797248",
    
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
        pred = prediction['displayNames']
        return pred


image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if image is not None:
    # Convert the UploadedFile object to bytes
    r = predict_image_classification_sample(image)
    for i in r:
        st.write(i)
