import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    with open('fertilizer_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'fertilizer_model.pkl' is in the same directory.")
    st.stop()

# Title and header for the app
st.title("Fertilizer Recommendation System 🌱")
st.write("Enter the soil and crop details to get a fertilizer recommendation.")

# --- Create input fields for user ---

# Mapping dictionaries for categorical features (must match the original encoding)
soil_map = {'Black': 0, 'Clayey': 1, 'Loamy': 2, 'Red': 3, 'Sandy': 4}
crop_map = {
    'Barley': 0, 'Cotton': 1, 'Ground Nuts': 2, 'Maize': 3, 'Millets': 4,
    'Oil seeds': 5, 'Paddy': 6, 'Pulses': 7, 'Sugarcane': 8, 'Tobacco': 9, 'Wheat': 10
}

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    temp = st.slider("Temperature (°C)", 20, 40, 26)
    humidity = st.slider("Humidity (%)", 50, 70, 60)
    moisture = st.slider("Moisture (%)", 30, 70, 50)
    soil_type_str = st.selectbox("Soil Type", list(soil_map.keys()))

with col2:
    crop_type_str = st.selectbox("Crop Type", list(crop_map.keys()))
    nitrogen = st.slider("Nitrogen (N)", 0, 50, 25)
    potassium = st.slider("Potassium (K)", 0, 50, 25)
    phosphorous = st.slider("Phosphorous (P)", 0, 50, 25)


# --- Predict and display the result ---

if st.button("Recommend Fertilizer"):
    # Convert categorical inputs to their numerical encoded values
    soil_type = soil_map[soil_type_str]
    crop_type = crop_map[crop_type_str]

    # Create the input array for the model in the correct order
    input_data = np.array([[temp, humidity, moisture, soil_type, crop_type, nitrogen, potassium, phosphorous]])

    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"**The recommended fertilizer is: {prediction[0]}**")