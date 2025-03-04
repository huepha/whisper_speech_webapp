# WHISPER & SPEECH Web App

This is a web application that allows users to record audio, transcribe it using OpenAI's Whisper model, and convert the transcription to speech using an OpenAI Speech-compatible server. The app is built with HTML, CSS, and JavaScript.

## Features
- **Audio Recording**: Record audio directly in the browser.
- **Transcription**: Transcribe audio using OpenAI's Whisper model.
- **Text-to-Speech**: Convert transcribed text to speech using an OpenAI Speech-compatible server.
- **Edit Transcription**: Edit the transcribed text before converting it to speech.
- **Download Audio**: Download the generated speech as an MP3 file.

## Prerequisites
To run this web app, you need to set up two servers:
1. **Whisper Server**: For audio transcription.
2. **OpenAI Speech-Compatible Server**: For text-to-speech conversion.

### 1. Setting Up the Whisper Server
Follow the instructions in the [OpenAI Whisper GitHub repository](https://github.com/openai/whisper) to set up the Whisper server. Once the server is running, note the API endpoint (e.g., `https://localhost:5000/audio/transcriptions`).

### 2. Setting Up the OpenAI Speech-Compatible Server
Follow the instructions in the [OpenAI Speech-Compatible Server GitHub repository](https://github.com/matatonic/openedai-speech) to set up the text-to-speech server. Once the server is running, note the API endpoint (e.g., `https://localhost:8000/v1/audio/speech`).

## Running the Web App
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
