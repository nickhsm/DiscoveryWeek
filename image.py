from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st  # Voor de Streamlit componenten

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()


def image_process():
    # Kies tussen uploaden of webcam
    option = st.radio("Kies een methode:", ["Upload een foto", "Maak een foto met je webcam"])

    # Laad afbeelding afhankelijk van de keuze van de gebruiker
    image_data = st.file_uploader("Upload een afbeelding",
                                  type=["jpg", "jpeg", "png"]) if option == "Upload een foto" else st.camera_input(
        "Maak een foto")

    if image_data:
        # Verwerk de afbeelding voor model input
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Open de afbeelding (van de uploader of webcam input)
        image = Image.open(image_data).convert("RGB")

        # Resize en crop de afbeelding naar 224x224 pixels
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # Zet de afbeelding om naar een numpy array
        image_array = np.asarray(image)

        # Normaliseer de afbeelding
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Laad de afbeelding in de data array
        data[0] = normalized_image_array

        # Voorspel met het model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Toon de voorspelling en confidence score
        st.write(f"Voorspelde uilsoort: {class_name.strip()}")
        st.write(f"Zekerheid: {confidence_score:.2f}")


# Aanroepen van de functie binnen Streamlit
if __name__ == "__main__":
    st.title("Uilherkenning met AI")
    image_process()
