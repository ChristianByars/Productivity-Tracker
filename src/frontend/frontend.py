import streamlit as st
import pandas as pd

st.write("This is my Producitivity App:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))