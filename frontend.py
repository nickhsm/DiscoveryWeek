import streamlit as st
import audio
import image


with st.sidebar:
    st.logo("hootfinder.svg", size="large", link=None, icon_image=None)
    add_radio = st.radio(
            "Kies manier van herkenning",
            ["Foto", "Audio"]
            )

if add_radio == "Foto":
    image.image()
else:
    audio.audio()
