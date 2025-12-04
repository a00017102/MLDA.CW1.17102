import streamlit as st
import joblib
import pandas as pd
import numpy as np
import datetime

# Load model, scaler, and feature names
model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")


st.title("Bike Rental Prediction App for Seoul")
st.write("Adjust variables to roughly estimate bike rental count.")


hour = st.selectbox(
    "Hour of Day",
    options=list(range(0, 24)),
    format_func=lambda x: f"{x}:00"
)

col1, col2 = st.columns(2)
with col1:
    temperature = st.slider("Temperature (°C)", -17.8, 39.4, 13.7)
with col2:
    humidity = st.slider("Humidity (%)", 0, 98, 57)

col1, col2 = st.columns(2)
with col1:
    wind = st.slider("Wind speed (m/s)", 0.0, 7.4, 1.5)
    if wind < 1.5:
        st.caption("Calm wind")
    elif wind < 4.0:
        st.caption("Light breeze")
    else:
        st.caption("Strong wind")
with col2:
    visibility = st.slider("Visibility (10m)", 27, 2000, 1698)
    if visibility < 500:
        st.caption("Low visibility - might be foggy or dark")
    elif visibility < 1500:
        st.caption("Moderate visibility - partly clear")
    else:
        st.caption("High visibility - clear day")

col1, col2 = st.columns(2)
with col1:
    dew = st.number_input("Dew Point Temperature (°C)", -30.6, 27.2, 5.0)
    if dew < 0:
        st.caption("Very dry/cold air")
    elif dew < 10:
        st.caption("Cool and dry air")
    elif dew < 20:
        st.caption("Comfortable air")
    else:
        st.caption("Warm and humid air")
with col2:
    solar = st.number_input("Solar Radiation (MJ/m²)", 0.0, 3.52, 0.5)
    if solar < 0.5:
        st.caption("Cloudy/Low sunlight")
    elif solar < 2.0:
        st.caption("Partly sunny")
    else:
        st.caption("Sunny")

col1, col2 = st.columns(2)
with col1:
    rain = st.number_input("Rainfall (mm)", 0.0, 35.0, 0.0, step=0.1)
    if rain == 0:
        st.caption("No rain")
    elif rain < 10:
        st.caption("Light rain")
    else:
        st.caption("Heavy rain")
with col2:
    snow = st.number_input("Snowfall (cm)", 0.0, 8.8, 0.0, step=0.1)
    if snow == 0:
        st.caption("No snow")
    elif snow < 3:
        st.caption("Light snow")
    else:
        st.caption("Heavy snow")

col1, col2 = st.columns(2)
with col1:
    holiday = st.selectbox("Holiday?", ["No Holiday", "Holiday"])
    holiday = 1 if holiday == "Holiday" else 0
with col2:
    functioning = st.selectbox("Functioning Day?", ["Yes", "No"])
    functioning = 1 if functioning == "Yes" else 0

selected_date = st.date_input(
    "Select Date",
    value=datetime.date(2018, 7, 16),
    min_value=datetime.date(2017, 1, 1),
    max_value=datetime.date(2018, 12, 31)
)
year = selected_date.year
month = selected_date.month
day = selected_date.day
day_of_week = selected_date.weekday()  # 0=Monday, 6=Sunday
is_weekend = 1 if day_of_week >= 5 else 0
is_working = 1 if (7 <= hour <= 9) or (17 <= hour <= 19) else 0
temp_hour_interaction = temperature * hour
weather_comfort = int(
    (10 < temperature < 30)
    and rain == 0
    and snow == 0
)
season = st.selectbox("Season", ["Autumn", "Spring", "Summer", "Winter"])
season_map = {
    "Autumn": [1, 0, 0, 0],
    "Spring": [0, 1, 0, 0],
    "Summer": [0, 0, 1, 0],
    "Winter": [0, 0, 0, 1],
}
season_values = season_map[season]

# Prepare input for model
input_values = [
    hour, temperature, humidity, wind, visibility,
    dew, solar, rain, snow,
    holiday, functioning,
    year, month, day, day_of_week,
    is_weekend, is_working,
    temp_hour_interaction, weather_comfort
] + season_values

input_df = pd.DataFrame([input_values], columns=feature_names)
input_scaled = scaler.transform(input_df)

# Prediction
if st.button("Predict Bike Rentals"):
    prediction = model.predict(input_scaled)[0]
    key_inputs = {
        "Date": selected_date.strftime("%Y-%m-%d"),
        "Hour": f"{hour}:00",
        "Temperature (°C)": temperature,
        "Humidity (%)": humidity,
    }

    for key, value in key_inputs.items():
        st.markdown(f"<p><strong>{key}:</strong> {value}</p>", unsafe_allow_html=True)

    st.markdown(f"<h4 style='margin-top:15px;'>Predicted Rentals: {int(prediction)} bikes</h4>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
