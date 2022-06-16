import streamlit as st
import pandas as pd

st.write("Hola Mundo")

df = pd.DataFrame({"Columna 1": [1,2,3,4,5],
"Columna 2": [10,20,30,40,50]})

st.write(df)

