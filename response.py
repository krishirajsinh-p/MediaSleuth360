import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_response(prompt: str, system: str) -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        model="llama3-8b-8192"
    )
    # if error in response then display error message
    if "error" in response:
        return f"""[ERROR {response["error"]["type"]}]: {response["error"]["message"]}"""
    else:
        return response.choices[0].message.content