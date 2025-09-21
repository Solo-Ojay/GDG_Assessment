# app.py
import streamlit as st
import os
import pandas as pd
import pickle
from joblib import load

# Load trained model
BASE_DIR = os.path.dirname(__file__)

model = load(os.path.join(BASE_DIR, "whr_best_model.pkl"))
scaler = load(os.path.join(BASE_DIR, "whr_scaler.pkl"))
model_columns = load(os.path.join(BASE_DIR, "whr_model_columns.pkl"))

st.title("Happiness Score Predictor 🌏")

# --- User Inputs ---
country = st.selectbox("Country", model_columns['country_names'])
region = st.selectbox("Region", model_columns['region_names'])
year = st.number_input("Year", min_value=2015, max_value=2023, value=2023)
gdp_per_capita = st.number_input("GDP per capita", value=1.0)
life_expectancy = st.number_input("Healthy Life Expectancy", value=70.0)
social_support = st.number_input("Social Support", value=0.8)
freedom = st.number_input("Freedom to Make Life Choices", value=0.5)

# --- Prepare Input DataFrame ---
input_df = pd.DataFrame({
    'year': [year],
    'gdp_per_capita': [gdp_per_capita],
    'healthy_life_expectancy': [life_expectancy],
    'social_support': [social_support],
    'freedom_to_make_life_choices': [freedom],
    'country': [country],
    'region': [region]
})

# --- Preprocessing ---
# One-hot encode categorical variables with the same columns as training
numeric_features = model_columns['numeric_features']  
input_df[numeric_features] = scaler.transform(input_df[numeric_features])


# One-hot encode categorical columns (like during training)
input_df = pd.get_dummies(input_df, columns=['country', 'region'])

# Add missing columns at once
missing_cols = list(set(model_columns['all_features']) - set(input_df.columns))
if missing_cols:
    input_df = pd.concat([input_df, pd.DataFrame(0, index=input_df.index, columns=missing_cols)], axis=1)

# Reorder to match training
input_df = input_df[model_columns['all_features']]

# Scale numeric features
input_df[model_columns['numeric_features']] = scaler.transform(input_df[model_columns['numeric_features']])

# Predict
prediction = model.predict(input_df)
st.subheader(f"Predicted Happiness Score: {prediction[0]:.3f}")