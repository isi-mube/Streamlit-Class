import streamlit as st
import pandas as pd

### Basic Display ###
# Streamlit runs top to bottom
st.write('Hello, world!') # Basic body text
hello = st.write('Hello, world (as variable)!')
print(hello) # Display the variable hello


### Text Display ###
st.title('Text Display Basics') # title
st.header('Header') # Larger text
st.subheader('Subheader') # Smaller text
st.code('print("Hello, world!")') # Code block
st.markdown('**Markdown**') # Markdown
st.latex(r'\int_a^b f(x) dx') # LaTeX
st.write("Basic Text") # Horizontal rule

### Data Display ###
st.title('Data Display Basics') # title

# DataFrames (interactive)
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.dataframe(df)

# DataFrames (non-interactive)
st.table(df)

# JSON
st.json({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})