import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.title("Haciendo gráficos con altair en streamlit")

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.write(df.head(5))

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

