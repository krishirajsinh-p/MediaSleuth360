import streamlit as st
from raw_data import generate_raw
import time

def transcribe(raw_data) -> str:
    transcript=""
    for line in raw_data.segments:
        start_time = time.strftime('%H:%M:%S', time.gmtime(line['start']))
        end_time = time.strftime('%H:%M:%S', time.gmtime(line['end']))
        transcript += f"{start_time} - {end_time} : {line['text']}\n"
    return transcript

@st.cache_data()
def generate_transcript(file, filetype) -> str:
    raw_data = generate_raw(file, filetype)
    if type(raw_data) is str:
        return raw_data
    transcript = f"filetype: {filetype}\n"
    if type(raw_data) is not list:
        transcript += f"Total Duration: {time.strftime('%H:%M:%S', time.gmtime(raw_data.duration))}\n"
        transcript += f"Language: {raw_data.language}\n"
        transcript += f"\nTranscript:\n"
        transcript += transcribe(raw_data)
    else:
        transcript += f"Total Duration: {time.strftime('%H:%M:%S', time.gmtime(raw_data[-1].segments[-1]['end']))}\n"
        transcript += f"Language: {raw_data[0].language}\n"
        transcript += f"\nTranscript:\n"
        for chunk in raw_data:
            transcript += transcribe(chunk)
    return transcript