import streamlit as st
from response import generate_response
from transcribe import generate_transcript

@st.cache_data()
def generate_summary(file) -> str:
    transcript = generate_transcript(file)
    
    system_prompt = """You are a helpful assistant you should be able \
to generate a summary from the media transcript. The summary \
should have important chapters or topics disscussed in \
the media along with the timestamps.

you should follow the format give below:
start_time - end_time : Chapter 1 summary.
start_time - end_time : Chapter 2 summary.
start_time - end_time : Chapter 3 summary.
...


Overall summary of the media: <summary of the media>.

Note: strictly follow the format and do not include any other information.\
"""

    user_prompt = f"generate the summary from the media transcript:\n\n{transcript}"

    return generate_response(system_prompt, user_prompt)