
import streamlit as st
from gtts import gTTS

def create_audiobook(text, output_file):
    """Convert text to an audiobook and save it."""
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

# Streamlit app
st.title("Text-to-Audiobook Converter")

# File uploader for text files
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    # Display uploaded file content
    text = uploaded_file.read().decode('utf-8')
    st.text_area("File Content", text, height=300)

    # Convert button
    if st.button("Convert to Audiobook"):
        output_file = "audiobook.mp3"
        create_audiobook(text, output_file)

        # Provide a download link
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download Audiobook",
                data=file,
                file_name="audiobook.mp3",
                mime="audio/mpeg"
            )
