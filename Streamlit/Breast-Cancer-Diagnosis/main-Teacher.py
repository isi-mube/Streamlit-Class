import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

col_1, col_2, col_3 = st.columns([1, 2, 1])
with col_2: # middle column
    st.image("logo.png", width=200)  # logo

tabs = st.tabs(["Input", "Viz", "About"])

with tabs[0]:
    st.subheader("Inputs")
    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello, {name}! 👋")

    # Add a slider
    age = st.slider("How old are you?", 0, 100, 25)
    st.write(f"Your age is: {age}")
with tabs[1]:
    st.write("Viz")

    data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10)})

    # Line chart
    st.line_chart(data)

    # Bar chart
    st.bar_chart(data)

    # Apart from line_chart and bar_chart, you can also use other chart types:
    st.area_chart(data)
    st.altair_chart(data)

    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'], label='Random Data')
    ax.set_title("Custom Line Plot")
    ax.legend()

    st.pyplot(fig)
with tabs[2]:
    st.write("About")
    st.write("This is a Streamlit app for the DSML Master course.")
    st.write("Built with ❤️ by the DSML Master team.")
    # Add a button to do something funny:
    if st.button("Click me!"):
        st.balloons()