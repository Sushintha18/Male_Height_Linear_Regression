# Male Height Prediction using Linear Regression

## Project Overview

This project predicts the average male height based on country and year using the Linear Regression algorithm. The dataset was obtained from Kaggle and preprocessed using Python and Pandas. A Streamlit web application is used to interact with the trained model and generate predictions.

---

## Dataset

**Dataset Name:** Male Height Dataset

**Source:** Kaggle

### Features

| Feature | Description |
|----------|------------|
| ccode | Country Code |
| country.name | Country Name |
| year | Year of measurement |
| value | Average Male Height (Target Variable) |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib
- Kaggle API

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Downloaded dataset from Kaggle.
2. Loaded dataset into a Pandas DataFrame.
3. Checked dataset dimensions and structure.
4. Examined data types.
5. Checked for missing values.
6. Checked for duplicate records.
7. Applied One-Hot Encoding on:
   - `ccode`
   - `country.name`
8. Split dataset into training and testing sets.

---

## Model Building

### Algorithm Used

**Linear Regression**

### Steps

1. Define Features (X)
2. Define Target Variable (y)
3. Split data into Training and Testing sets
4. Train the Linear Regression model
5. Generate predictions
6. Evaluate model performance

---

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

## Streamlit Application

The Streamlit application allows users to:

- Select a Country
- Enter a Year
- Predict Average Male Height

### Input

- Country Name
- Year

### Output

- Predicted Male Height (cm)

---

## Project Structure

```text
male_height_linear_regression/
│
├── streamlit_app.py
├── requirements.txt
├── height_dataset.csv
├── README.md
└── screenshots/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/male_height_linear_regression.git
```

### Move to Project Directory

```bash
cd male_height_linear_regression
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

## Sample Workflow

1. Open the Streamlit application.
2. Select a country.
3. Enter a year.
4. Click **Predict Height**.
5. View the predicted male height.

---

## Future Enhancements

- Save trained model using Joblib
- Deploy model on Streamlit Cloud
- Add data visualizations
- Compare multiple machine learning algorithms
- Improve prediction accuracy

---

## Author

**Sushintha S**

---

## License

This project is developed for educational and learning purposes.
