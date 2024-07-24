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

    # If generate_raw returns string error, return it as is
    if type(raw_data) is str:
        return raw_data
    
    transcript = f"File Type: {filetype}\n"
    if type(raw_data) is not list:
        transcript += f"Total Duration: {time.strftime('%H:%M:%S', time.gmtime(raw_data.duration))}\n"
        transcript += f"Language: {raw_data.language}\n\n"
        transcript += f"Transcript:\n"
        transcript += transcribe(raw_data)
    else:
        transcript += f"Total Duration: {time.strftime('%H:%M:%S', time.gmtime(raw_data[-1].segments[-1]['end']))}\n"
        transcript += f"Language: {raw_data[0].language}\n\n"
        transcript += f"Transcript:\n"
        for chunk in raw_data:
            transcript += transcribe(chunk)

    return transcript

def generate_subtitle_file(file, filetype):
    raw_data = generate_raw(file, filetype)

    # If generate_raw returns string error, exit
    if type(raw_data) is str:
        return

    if type(raw_data) is not list:
        with open('media.vtt', 'w') as f:
            f.write("WEBVTT\n\n")
            for line in raw_data.segments:
                start_time = time.strftime('%H:%M:%S', time.gmtime(line['start']))
                end_time = time.strftime('%H:%M:%S', time.gmtime(line['end']))
                f.write(f"{line['id'] + 1}\n")
                f.write(f"{start_time}.000 --> {end_time}.000\n")
                f.write(f"{line['text']}\n\n")
    else:
        i = 1
        with open('media.vtt', 'w') as f:
            f.write("WEBVTT\n\n")
            for chunk in raw_data:
                for line in chunk.segments:
                    start_time = time.strftime('%H:%M:%S', time.gmtime(line['start']))
                    end_time = time.strftime('%H:%M:%S', time.gmtime(line['end']))
                    f.write(f"{i}\n")
                    f.write(f"{start_time}.000 --> {end_time}.000\n")
                    f.write(f"{line['text']}\n\n")
                    i += 1