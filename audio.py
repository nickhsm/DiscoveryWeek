import streamlit as st
import audio_processing

def audio():
    '''
    Page that used for audio recognition.
    '''
    st.title("Audio herkenning")
    
    with st.form(key="test"):
        audio_path = st.file_uploader("Upload hier de audio bestand",
                                      type=["wav"]
                                      )
        submit_button = st.form_submit_button(label="Start")

    if submit_button:
        results = audio_processing.audio_process(audio_path)
        st.write(results)
