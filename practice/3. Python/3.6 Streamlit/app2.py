import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
st.button("Click me")
st.menu_button("Export", options=["CSV", "JSON", "PDF"])


st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.datetime_input("Event date and time")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.color_picker("Pick a color")
# 2. Multi-column Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Field")
    user_text = st.text_input("Type something:", "Streamlit is fun")
    st.write(f"Reversed Text: {user_text[::-1]}")

with col2:
    st.subheader("Conditional Logic")
    show_metrics = st.checkbox("Show Data Metrics")
    if show_metrics:
        st.metric(label="Accuracy", value="94.2%", delta="1.5%")
        st.metric(label="Latency", value="120ms", delta="-15ms")

st.pagination(10)

import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.line_chart(df)

st.cache_data.clear()
st.cache_resource.clear()
