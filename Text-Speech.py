import streamlit as st
from gtts import gTTS

def create_audiobook(text, output_file):
    """Convert text to an audiobook and save it."""
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

# Streamlit app
st.title("Text-to-Audiobook Converter")

# Text area for user input
text = st.text_area("Paste your text below:", height=300)

# Convert button
if st.button("Convert to Audiobook"):
    if text.strip():
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
    else:
        st.error("Please paste some text before converting.")
