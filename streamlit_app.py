# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = joblib.load(r'E:\celebal assignments\assignment 7\model.pkl')
iris = load_iris()

# Title
st.title("🌸 Iris Flower Prediction App")

st.markdown("Input features to predict the Iris species.")

# Input form
sepal_length = st.slider('Sepal length (cm)', 4.0, 8.0, 5.4)
sepal_width = st.slider('Sepal width (cm)', 2.0, 4.5, 3.4)
petal_length = st.slider('Petal length (cm)', 1.0, 7.0, 1.3)
petal_width = st.slider('Petal width (cm)', 0.1, 2.5, 0.2)

# Prediction
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    pred_class = iris.target_names[prediction[0]]
    st.success(f"Predicted Iris species: **{pred_class}**")

# Visualization
st.subheader("📊 Feature Distributions")
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

selected_feature = st.selectbox("Choose a feature to visualize", df.columns[:-1])
fig, ax = plt.subplots()
sns.histplot(data=df, x=selected_feature, hue='species', kde=True, ax=ax)
st.pyplot(fig)
