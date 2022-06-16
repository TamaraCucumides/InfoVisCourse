import streamlit as st

# Slider
st.write("Un slider")
x = st.slider('x')

st.write(x, "por 10 es", x*10)

# Checkbox
if st.checkbox("Informacion oculta"):
    st.write("Accediste a la informacion oculta")

# Select
option = st.selectbox("Que fruta te gusta más?", ["Manzana", "Pera", "Naranja"])

st.write("Seleccionaste la:", option)
