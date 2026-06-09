import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("height_dataset.csv", delimiter=";", decimal=",")

# Save country list before encoding
countries = sorted(df["country.name"].unique())

# One-hot encoding
df_encoded = pd.get_dummies(
    df,
    columns=["ccode", "country.name"],
    drop_first=True
)

# Features and target
X = df_encoded.drop("value", axis=1)
y = df_encoded["value"]

# Train model
model = LinearRegression()
model.fit(X, y)

st.title("Male Height Prediction")

# User inputs
year = st.number_input(
    "Enter Year",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    value=2000
)

country = st.selectbox(
    "Select Country",
    countries
)

# Prediction button
if st.button("Predict Height"):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=X.columns
    )

    input_df["year"] = year

    country_col = f"country.name_{country}"

    if country_col in input_df.columns:
        input_df[country_col] = 1

    prediction = model.predict(input_df)[0]

    st.success(
        f"Predicted Male Height: {prediction:.2f} cm"
    )
