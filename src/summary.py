import streamlit as st
from response import generate_response
from transcribe import generate_transcript

@st.cache_data()
def generate_summary(file, filetype) -> str:
    """
    Generate a structured summary of the given file.

    Args:
        file (str): The path to the file.
        filetype (str): The type of the file.

    Returns:
        str: The generated summary.

    """
    system_prompt = f"""You are an expert media analyst. Your task is \
to create a structured summary of the {filetype}. The summary should \
include key chapters or topics, each with corresponding timestamps.

Note: Ensure the summary is concise and focuses on the main points. \
Strictly adhere to the context and do not include any additional information or commentary. \
Summary timestamps can't exceed the total duration of the {filetype}.
"""

    user_prompt = f"""Generate summary for the {filetype} content provided below, \
identify key chapters or topics discussed along with their timestamps:\
\n\n{generate_transcript(file, filetype)}"""

    return generate_response(system_prompt, user_prompt)