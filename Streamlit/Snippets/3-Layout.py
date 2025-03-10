import streamlit as st
import time


### Layout ###
# Sidebar
name = st.sidebar.text_input("Enter your name")
st.sidebar.write(f"Hello, {name}!")

# Columns
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

with st.expander("Click to expand"):
    st.write("Expanded content")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content in Tab 1")
    st.video("data/cat-video.mp4")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)

    with st.spinner("Loading..."):
        time.sleep(2)
    st.success("Done!")
with tab2:
    st.write("Content in Tab 2")
    with st.form("my_form"):
        name = st.text_input("Enter your name")
        submit = st.form_submit_button("Submit")

        if submit:
            st.write(f"Hello, {name}!")
