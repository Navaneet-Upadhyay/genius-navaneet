# Genius Navaneet 🎙️

Genius Navaneet is a Python-based voice assistant that listens to voice commands and performs different tasks such as opening websites, playing music, fetching news, and answering questions using Google Gemini AI.

## Features

- 🎤 Voice command recognition
- 🌐 Open websites such as Google, YouTube, Facebook, LinkedIn and ChatGPT
- 🎵 Play songs using voice commands
- 📰 Fetch and read the latest news
- 🤖 Answer general questions using Google Gemini AI
- 🔊 Text-to-speech responses

## Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Feedparser
- Google Gemini API
- Webbrowser

## Installation

### 1. Clone the repository

    git clone https://github.com/Navaneet-Upadhyay/genius-navaneet.git

### 2. Install required packages

    pip install -r requirements.txt

## API Key Setup

This project uses the Google Gemini API.

Create a `.env` file in the project folder:

    GEMINI_API_KEY=your_api_key_here

Do not upload your `.env` file or API key to GitHub.

## Run the Project

Run:

    python main.py

Make sure your microphone is connected and working.

## Project Structure

    genius-navaneet/
    │
    ├── main.py
    ├── gemini.py
    ├── musicLibrary.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Future Improvements

- Add more voice commands
- Improve AI conversation
- Add more automation features
- Improve error handling
- Add more useful integrations

## License

This project is created for learning and personal development.