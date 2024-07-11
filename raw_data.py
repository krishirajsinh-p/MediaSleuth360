import streamlit as st
from groq import Groq
from moviepy.editor import VideoFileClip
import tempfile
import os

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def extract_audio(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(file.getbuffer())
        temp_video_path = temp_video.name
    
    # Convert video to audio using MoviePy
    video_clip = VideoFileClip(temp_video_path)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio:
        temp_audio_path = temp_audio.name
        video_clip.audio.write_audiofile(temp_audio_path)
    
    # Remove the temporary video file
    os.remove(temp_video_path)

    # Open the converted audio file
    with open(temp_audio_path, 'rb') as audio_file:
        audio_bytes = audio_file.read()
    
    return (temp_audio_path, audio_bytes)

@st.cache_data()
def generate_raw(file, filetype):
    # If the file is a video, convert it to audio first
    if filetype.startswith('video/'):
        file = extract_audio(file)

    # Generate the raw data
    raw = client.audio.transcriptions.create(
        file=file,
        model="whisper-large-v3",
        response_format="verbose_json"
    )
    
    # Remove the temporary audio file
    os.remove(file[0])

    return raw