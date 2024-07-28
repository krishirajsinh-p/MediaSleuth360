<div align="center">
    <h1>
        🔎 MediaSleuth360
    </h1>
    MediaSleuth360 aims to revolutionize how users interact with media content by leveraging advanced AI technologies. The platform can be the go-to tool for extracting, understanding, and navigating information from video and audio files, enhancing productivity and accessibility for users across various domains, including education, content creation, and entertainment.
</div>

## Website 🌐

> [!NOTE]
> It uses free APIs so It may run out of free quote quickly.

For small media files(~10 mins or less) you can use https://mediasleuth360.infinityfreeapp.com/. For larger files follow setup instructions given below and run locally with your API keys.

## Demo Video 🎥
https://github.com/user-attachments/assets/723a7660-ad6c-42bd-9ce6-d1693f3b69b9

## System Workflow 💻🏗️

![System_Workflow](https://github.com/user-attachments/assets/e4bdde2b-45b8-4049-ab44-97ae000b5ec1)

1.	**User Uploads Media**: The user uploads an audio or video file through the Streamlit interface.
2.	**Processing**:
    - The main.py script calls functions from raw_data.py to extract raw data from the media.
    - transcribe.py is used to generate transcripts and subtitle files.
    - summary.py provides a summary of the media content.
    - response.py generates responses to user queries about the media.
3.	**User Interaction**: The application displays the media player, transcript, and summary. Users can ask questions about the media content, and the application responds using the generate_chat_response function.

## Features ✨

- **Media Support**: Support almost any video or audio file format.
- **Time Stamping**: Automatically generates a transcript for the media.
- **Subtitles Generation**: Automatically adds subtitles to the video.
- **Summarization**: Provides a concise structered summary of the media content with timestamps for broader picture.
- **Interactive Chatbot**: An interactive chatbox allows users to engage with the AI to query specific topics within the media content.
- **Media Navigation**: Users can ask AI to search for specific keywords/topics/bits within the media.
- **Multilingual Media Analysis**: Supports analysis of media content in multiple languages, enhancing accessibility and usability.
- **Caching**: The smart caching media content will make processing much faster when user uploads the same file.
- **CI/CD**: This is developed in Python with Streamlit which by design enables CI and CD during development and testing.

## Tools 🛠

**Software Dependencies**
- [Python v3.10.12](https://www.python.org/)
- [ffmpeg v4.4.2](https://www.ffmpeg.org/)

**Python Dependencies**:
- [streamlit v1.36.0](https://streamlit.io/)
- [groq v0.9.0](https://groq.com/)
- [google-generativeai v0.7.2](https://pypi.org/project/google-ai-generativelanguage/)
- [moviepy v1.0.3](https://pypi.org/project/moviepy/)
- [pydub v0.25.1](https://pydub.com/)

**AI Models**:
- [llama3-8b-8192](https://huggingface.co/meta-llama/Meta-Llama-3-8B) via Groq API
- [whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) via Groq API
- [gemini-1.5-flash](https://deepmind.google/technologies/gemini/flash/) via Google API

## Setup ⚙️ (Currently only for unix based OS)

### Step 1: Clone the repository

```bash
git clone https://github.com/krishirajsinh-p/MediaSleuth360.git
```

### Step 2: Go to project's root directory

```bash
cd MediaSleuth360
```

### Step 3: Install dependencies

```bash
bash install.sh
```

### Step 4: Add API keys

Place your [Groq](https://groq.com/) and [Google](https://aistudio.google.com/app/apikey) API keys in ./.streamlit/secrets.toml

### Step 5: Run program and access the platform

```bash
bash run.sh
```

### Step 6: Access the platform

> [!NOTE]
> Port number might be different but you will find it in the terminal when you run the above given command

open in browser http://localhost:8501

## Limitations ⚠️

- **Reliance on Speech Quality**: The effectiveness of the system heavily depends on the quality of the input speech.
- **File Size**: There is a 200MB media file size limit due to Streamlit constraints.
- **Language Support**: It may not work **as effectively** for languages other than English.
- **No Memory**: The AI assistant don't have conversational memory because of the limited context window of the LLM model(also to minimize security concerns and resource usage).

## License

MediaSleuth360's code is released under the MIT License. See [LICENSE](https://github.com/krishirajsinh-p/MediaSleuth360/blob/master/LICENSE) for further details.
