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
    option = st.radio("Kies een methode:", ["Upload een foto", "Maak een foto met je webcam"])
    image_data = st.file_uploader("Upload een afbeelding",
                                  type=["jpg", "jpeg", "png"]) if option == "Upload een foto" else st.camera_input("Maak een foto")
    if image_data:
        class_name, confidence_score = image.image_process(image_data)
        st.write(f"Voorspelde vogelsoort: {class_name}")
        st.write(f"Zekerheid: {confidence_score:.2f}")

else:
    audio.audio()
