import streamlit as st
from groq import Groq
import google.generativeai as genai

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config=genai.GenerationConfig(
        temperature=0.1,
        top_p=0.95
    )
)

def generate_response(system: str, prompt: str) -> str:
    try:
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
            model="llama3-8b-8192",
            temperature=0.1,
            top_p=0.95,
        )
        return response.choices[0].message.content
    except Exception as e:
        try:
            safe = [
                {
                    "category": "HARM_CATEGORY_DANGEROUS",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE",
                },
            ]
            response = model.generate_content([system, prompt], safety_settings=safe)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"
