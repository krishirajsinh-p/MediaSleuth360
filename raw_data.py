import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache_data()
def generate_raw(file):
    raw = client.audio.transcriptions.create(
        file=file,
        model="whisper-large-v3",
        response_format="verbose_json"
    )
    return raw