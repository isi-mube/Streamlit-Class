import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
@st.cache_data
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = [iris.target_names[i] for i in iris.target]
    return df, iris

df, iris = load_data()

# Sidebar Navigation
st.sidebar.title("ML Model Testing")
menu = st.sidebar.radio("Select an option:", ["Data Overview", "Model Testing"])

# Main Section
st.title("Iris Dataset - ML Model Testing")

if menu == "Data Overview":
    st.subheader("Explore the Iris Dataset")
    
    # Dataset preview
    st.dataframe(df)
    
    # Scatter plot
    fig = px.scatter(df, x="sepal length (cm)", y="sepal width (cm)", color="species", title="Sepal Length vs Width")
    st.plotly_chart(fig)

    # Dataset Statistics
    st.write("Dataset Statistics")
    st.write(df.describe())

elif menu == "Model Testing":
    st.subheader("Test ML Models on the Iris Dataset")

    # Tabs for different classifiers
    tab1, tab2 = st.tabs(["Random Forest", "Support Vector Machine"])

    with tab1:
        st.write("Random Forest Classifier")

        # User Inputs
        n_estimators = st.slider("Number of Trees", 10, 200, 50, step=10)
        max_depth = st.slider("Max Depth", 1, 10, 5)
        
        # Train Model
        X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
        model_rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model_rf.fit(X_train, y_train)
        predictions_rf = model_rf.predict(X_test)

        # Display Metrics
        acc_rf = accuracy_score(y_test, predictions_rf)
        st.metric(label="Model Accuracy", value=f"{acc_rf:.2%}")
        st.text("Classification Report:")
        st.text(classification_report(y_test, predictions_rf, target_names=iris.target_names))

    with tab2:
        st.write("Support Vector Machine")

        # User Inputs
        kernel = st.selectbox("Kernel Type", ["linear", "poly", "rbf", "sigmoid"])
        C = st.slider("Regularization (C)", 0.1, 10.0, 1.0)

        # Train Model
        model_svm = SVC(kernel=kernel, C=C, random_state=42)
        model_svm.fit(X_train, y_train)
        predictions_svm = model_svm.predict(X_test)

        # Display Metrics
        acc_svm = accuracy_score(y_test, predictions_svm)
        st.metric(label="Model Accuracy", value=f"{acc_svm:.2%}")
        st.text("Classification Report:")
        st.text(classification_report(y_test, predictions_svm, target_names=iris.target_names))

# Footer
st.sidebar.info("Adjust the parameters and explore different ML models in the tabs above.")