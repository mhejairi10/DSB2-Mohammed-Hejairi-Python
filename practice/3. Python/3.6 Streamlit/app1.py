
import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

import datetime








st.balloons()


    
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))





st.write("Your birthday is:", d)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")



st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.map(df, color='#ffaa00')



df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df)

st.title("My First APP")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.badge("Pythonista", color="blue")

st.cache_data.clear()
st.cache_resource.clear()