import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn import datasets

@st.cache_data
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = [iris.target_names[i] for i in iris.target]
    return df

df = load_data()

st.markdown(
    """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
        .stMarkdown, .stPlotlyChart, .stDataFrame {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Interactive Data Visualization Dashboard")

tab1, tab2, tab3 = st.tabs(["📌 Summary", "📈 Charts", "📋 Table View"])

with tab1:
    st.subheader("📌 Dataset Summary")
    st.write("This dashboard visualizes the Iris dataset with interactive charts and tables.")
    st.write("### 📊 Data Overview")
    st.write(df.describe())
    st.metric("Total Samples", df.shape[0])
    st.metric("Total Features", df.shape[1] - 1)

with tab2:
    st.subheader("📈 Data Visualization")
    chart_type = st.radio("Select Chart Type", ["Scatter Plot", "Box Plot"])

    if chart_type == "Scatter Plot":
        fig = px.scatter(df, x="sepal length (cm)", y="sepal width (cm)", color="species", title="Sepal Length vs. Width")
    else:
        fig = px.box(df, x="species", y="sepal length (cm)", title="Sepal Length Distribution by Species")

    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("📋 Dataset Table View")
    st.dataframe(df, use_container_width=True)
