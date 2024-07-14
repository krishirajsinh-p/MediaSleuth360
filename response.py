import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_response(system: str, prompt: str) -> str:
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
    try:
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# import google.generativeai as genai
# 
# genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# model = genai.GenerativeModel(
#     model_name="models/gemini-1.5-flash",
#     generation_config=genai.GenerationConfig(temperature=0.1, top_p=0.95)
# )

# def generate_response(prompt: str, system: str) -> str:
#     try:
#         response = model.generate_content([system, prompt])
#         print(response)     #remove this line
#         if response.candidates and response.candidates[0].safety_ratings:
#             # Check if the content is blocked due to safety concerns
#             if any(rating.blocked for rating in response.candidates[0].safety_ratings):
#                 return "Content blocked due to safety concerns."
#         # Check if there are valid parts in the response
#         if response.candidates and response.candidates[0].content:
#             return response.text
#         else:
#             return "No valid response generated."
#     except Exception as e:
#         return f"An error occurred: {e}"