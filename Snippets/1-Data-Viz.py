# Data Display II: Charts and plots
import streamlit as st
import pandas as pd
# Data Display III: Matplotlib, Plotly, Altair
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from sklearn import datasets
# pip install folium, streamlit-folium
import folium # interactive maps
from streamlit_folium import folium_static # folium to streamlit

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

### Data Display II: Charts and plots ###
st.title('Data Display II: Charts and Plots')
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

### Data Display III: Matplotlib, Plotly, Altair ###
st.title('Data Display III: Matplotlib, Plotly, Altair')
# Load the Iris dataset
iris = datasets.load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['species'] = [iris.target_names[i] for i in iris.target]

# Matplotlib Example
st.subheader("Matplotlib")
fig, ax = plt.subplots()
ax.scatter(df_iris["sepal length (cm)"], df_iris["sepal width (cm)"], 
           c=df_iris.index, cmap="viridis", alpha=0.7)
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
ax.set_title("Iris Dataset - Sepal Length vs. Width (Matplotlib)")
st.pyplot(fig) # Show the plot in Streamlit

# Plotly Example
st.subheader("Plotly")
fig_plotly = px.scatter(df_iris, 
                        x="sepal length (cm)", 
                        y="sepal width (cm)", 
                        color="species", 
                        title="Iris Dataset - Sepal Length vs. Width (Plotly)")
st.plotly_chart(fig_plotly)

### Data Display IV: Maps & Geospatial Data ###
### Maps & Geospatial Data ###
st.title('Maps & Geospatial Data')

# Basic Streamlit Map
st.subheader("Basic Map")
df_map = pd.DataFrame({'lat': [37.7749, 40.7128, 34.0522], 'lon': [-122.4194, -74.0060, -118.2437]})
st.map(df_map)

# Folium Interactive Map
st.subheader("Interactive Map")
m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)
folium.Marker([37.7749, -122.4194], popup="San Francisco").add_to(m)
folium_static(m)