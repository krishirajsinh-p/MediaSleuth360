import streamlit as st
from groq import Groq
from moviepy.editor import VideoFileClip
import tempfile
import os
from pydub import AudioSegment
from io import BytesIO
from streamlit.runtime.uploaded_file_manager import UploadedFileRec, UploadedFile
from streamlit.proto.Common_pb2 import FileURLs as FileURLsProto

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def extract_audio(file):
    """
    Extracts audio from a video file.

    Args:
        file (BytesIO): The video file.

    Returns:
        UploadedFile: The uploaded audio file.
    """
    # Save the uploaded video file as a temporary file
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

    # Remove the temporary audio file
    os.remove(temp_audio_path)

    # Create an UploadedFile object from the audio bytes
    mock_file_urls = FileURLsProto()
    uploaded_audio = UploadedFile(
        record=UploadedFileRec(
            file_id="mock_id",
            name="audio.mp3",
            type="audio/mpeg",
            data=audio_bytes
        ),
        file_urls=mock_file_urls
    )
    
    return uploaded_audio

def split_audio(file, chunk_duration_minutes=20) -> list:
    """
    Split the audio file into chunks of the specified duration.

    Args:
        file (BytesIO): The uploaded audio file as a BytesIO object.
        chunk_duration_minutes (int, optional): The duration of each chunk in minutes. Defaults to 20.

    Returns:
        list: A list of chunk names (file paths) for the split audio chunks.
    """
    # Read the content of the uploaded file as bytes and Convert them to a BytesIO object
    audio = AudioSegment.from_file(BytesIO(file.getvalue()))
    chunk_duration_ms = chunk_duration_minutes * 60 * 1000
    
    chunks = []
    # Split the audio into chunks of the specified duration
    for i, chunk in enumerate(audio[::chunk_duration_ms]):
        chunk_name = f"chunk_{i}.mp3"
        chunk.export(chunk_name, format="mp3")
        chunks.append(chunk_name)
    
    return chunks

def adjust_timestamps(chunk, time_offset: int):
    """
    Adjusts the timestamps of a chunk of transcribed audio.

    Args:
        chunk (Chunk): The chunk of transcribed audio.
        time_offset (int): The time offset to be added to the timestamps.

    Returns:
        Chunk: The adjusted chunk of transcribed audio.
    """
    for segment in chunk.segments:
        segment['start'] += time_offset
        segment['end'] += time_offset
    return chunk

@st.cache_data()
def generate_raw(file, filetype):
    """
    Generates raw data from an audio or video file.

    Args:
        file (BytesIO): The audio or video file.
        filetype (str): The type of the file ("audio" or "video").

    Returns:
        list: List of raw transcriptions.
    """
    # If the file is a video, convert it to audio first
    if filetype == "video":
        file = extract_audio(file)

    if file.size / (1024 ** 2) < 25.0:
        # Generate the raw data
        try:
            raw = client.audio.transcriptions.create(
                file=file,
                model="whisper-large-v3",
                response_format="verbose_json"
            )
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        # Split the audio into chunks
        chunks = split_audio(file)
        
        raw = []
        # Transcribe the remaining chunks with the previous transcription as a prompt and start time
        for i in range(0, len(chunks)):
            if i > 0:
                prompt = " ".join([segment['text'] for segment in raw[-1].segments[-2:]])
            else:
                prompt = None
            
            try:
                raw.append(
                    client.audio.transcriptions.create(
                        file=open(chunks[i], "rb"),
                        model="whisper-large-v3",
                        response_format="verbose_json",
                        prompt=prompt
                    )
                )
                raw[i] = adjust_timestamps(raw[i], i * 20 * 60)

                # Remove the temporary chunk files
                os.remove(chunks[i])
            except Exception as e:
                os.remove(chunks[i])

                return f"An error occurred: {e}"

    return raw