# MediaSleuth360
MediaSleuth360 aims to leverage AI for enhancing media content interaction, making it easier for users to find specific information in video or audio files.

## Features

- Media Upload: Users can upload video or audio files to the platform.
- Chatbox Interface: A chatbox will allow users to engage with the AI to query about specific topics within the media content.
- AI Assistance: The AI chatbot will analyze the uploaded media content and generate responses to user queries, providing relevant timestamps for the discussed topics.
- Time Stamping: The AI will identify key moments in the media file and correlate them with user queries, offering the timestamps for easy navigation.
- Search Functionality: Users can search for specific keywords or topics within the media content, and the AI will provide corresponding timestamps.
- Mulilingual media analysis

## Approach

flowchart diagram will go here

## Setup

how to run steps

python version 3.10.12
dependencies in requirements.txt

models: llama3-7b-8192, gemini-1.5-flash, whisper-v3-large

## To-Do List

- [x] make GUI
- [x] make chatbot work
- [x] deploy
- [x] add requirements.txt
- [x] generate summary with the timestamps
- [x] chatbot should only respond to the prompts relevent to the media
- [x] supports media in other languages other than english
- [x] error handling
- [x] whisper has 25mb limit, need to handle that
- [ ] documentation for the project

## License

MediaSleuth360's code is released under the MIT License. See [LICENSE](https://github.com/krishirajsinh-p/MediaSleuth360/blob/master/LICENSE) for further details.