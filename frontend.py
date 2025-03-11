import streamlit as st
import audio
import image


with st.sidebar:
    add_radio = st.radio(
            "Kies manier van herkenning",
            ["Foto", "Audio"]
            )

if add_radio == "Foto":
    image.image()
else:
    audio.audio()
