import streamlit as st
import pandas as pd

### Media Elements: Images, Audio, Video ###
st.title('Media Elements: Images, Audio, Video')
st.subheader('Images')
st.image("data/cat.jpg", caption="Sample Image", use_container_width=True)

st.subheader('Audio')
st.audio("data/cat-meow.mp3")

st.subheader('Video')
st.video("data/cat-video.mp4")

## Widgets ##
st.title('Widgets')
st.subheader('Buttons')
if st.button("Click Me!"):
    st.write("Button clicked!")

st.subheader('Checkbox')
agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")

st.subheader('Radio')
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You selected: {age}")

st.subheader('Selectbox')
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

st.subheader('Selectbox')
fruit = st.selectbox("Pick a fruit", ["Apple", "Banana", "Cherry"])
st.write(f"You selected: {fruit}")

st.subheader('Multiselect')
multiple_fruits = st.multiselect("Pick multiple fruits", ["Apple", "Banana", "Cherry"])
st.write(f"You selected: {multiple_fruits}")
