import streamlit as st
from raw_data import generate_raw
import time

@st.cache_data()
def generate_transcript(file, filetype) -> str:
    transcript = f"filetype: {filetype}\n\n"
    for line in generate_raw(file, filetype).segments:
        start_time = time.strftime('%H:%M:%S', time.gmtime(line['start']))
        end_time = time.strftime('%H:%M:%S', time.gmtime(line['end']))
        transcript += f"{start_time} - {end_time} : {line['text']}\n"
    return transcript