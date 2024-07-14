import streamlit as st
from response import generate_response
from transcribe import generate_transcript

@st.cache_data()
def generate_summary(file, filetype) -> str:
    system_prompt = f"""You are an expert media analyst. Your task is \
to create a structured summary of the {filetype}. The summary should \
include key chapters or topics, each with corresponding timestamps. \
Follow the exact format provided below:

start_time - end_time: Topic 1 summary.\n
start_time - end_time: Topic 2 summary.\n
start_time - end_time: Topic 3 summary.\n

Note: Ensure the summary is concise and focuses on the main points. \
Strictly adhere to the format and sepreate each topic with newline and \
do not include any additional information or commentary. Summary timestamps \
can't exceed the total duration of the {filetype}.
"""

    user_prompt = f"""Generate a structured summary for the {filetype} \
content provided below, identifying key chapters or topics discussed \
along with their timestamps:\n\n{generate_transcript(file, filetype)}\n\n"""

    return generate_response(system_prompt, user_prompt)