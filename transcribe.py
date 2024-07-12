import streamlit as st
from raw_data import generate_raw
import time

@st.cache_data()
def generate_transcript(file, filetype) -> str:
    # get file duration in HH:MM:SS format
    raw_data = generate_raw(file, filetype)
    transcript = f"""filetype: {filetype}
Total Duration: {time.strftime('%H:%M:%S', time.gmtime(raw_data.duration))}
Language: {raw_data.language}
\n\nTranscript:\n"""
    for line in raw_data.segments:
        start_time = time.strftime('%H:%M:%S', time.gmtime(line['start']))
        end_time = time.strftime('%H:%M:%S', time.gmtime(line['end']))
        transcript += f"{start_time} - {end_time} : {line['text']}\n"
    return transcript