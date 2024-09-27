# main.py

import streamlit as st
import pickle
import os

# Set file paths
MODEL_PATH = "spam_model.pkl"

# Function to load model
def load_model(model_path):
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}. Please check the path.")
        return None
    
    try:
        model = pickle.load(open(model_path, "rb"))
    except pickle.UnpicklingError:
        st.error("Error loading the model. The file might be corrupted.")
        return None

    return model

# Load the model
model = load_model(MODEL_PATH)

if model is None:
    st.stop()  # Stop if the model isn't loaded correctly

# Streamlit app interface
st.title("SMS Spam Classifier")
st.write("Enter an SMS message to classify it as spam or not spam.")

# Input text box for SMS message
input_message = st.text_area("Message", "")

# Classify the message when button is clicked
if st.button("Classify"):
    if input_message:
        prediction = model.predict([input_message])[0]  # Predict directly using the pipeline
        
        # Output the result
        if prediction == 1:
            st.error("This message is SPAM.")
        else:
            st.success("This message is NOT SPAM.")
    else:
        st.warning("Please enter a message.")
