# Voice-Enabled Conversational Chatbot 🤖🎤

A **voice-responsive chatbot** built using **Streamlit** and **OpenAI's speech-to-text and text-to-speech APIs**. Users can speak to the chatbot, and it responds audibly, enabling natural, interactive conversations.

---

## 🚀 Features

- Real-time **voice input and output** using OpenAI services  
- Text-to-speech and speech-to-text integration for natural conversations  
- **Streamlit web interface** with a chat-like UI  
- Floating interface elements for an enhanced user experience  
- Context-aware responses using GPT models  

---

## 🛠️ Tech Stack

- **Frontend / Interface:** Streamlit  
- **Backend / Processing:** Python  
- **AI / Speech Services:** OpenAI (Whisper for STT, TTS for speech generation, GPT-3.5 for responses)  
- **Audio Recording:** `audio_recorder_streamlit`  
- **Floating UI Elements:** `streamlit-float`  

---

## 📁 Project Structure

```
Voice Enabled Chatbot/
│
├── app.py # Streamlit application
├── utils.py # Functions for STT, TTS, and chatbot responses
├── requirements.txt # Python dependencies
├── .env # OpenAI API key
└── README.md # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice-chatbot.git
cd voice-chatbot
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### Key libraries include:
- streamlit – for building the web app
- openai – for AI services (STT, TTS, chatbot)
- audio_recorder_streamlit – record audio inside Streamlit
- streamlit-float – floating UI elements

### 3. Set Up Environment Variables

Create a .env file in the project root:
```
OPENAI_API_KEY='your_openai_api_key_here'
```
Keep this file private. Do not push it to GitHub.

### 4. Run the Streamlit App
```
streamlit run app.py
```
- The app will open in your default browser (usually at http://localhost:8501)
- Click the microphone button to record your voice
- Chatbot will transcribe, process, and respond with audio

## 🧩 How It Works

- User speaks into the microphone
- Audio is recorded and converted to text using speech_to_text
- Chatbot generates a response using get_answer (GPT model)
- Response text is converted to audio using text_to_speech
- Audio is played back to the user for a natural conversational experience


## ⚡ Functions Overview

- speech_to_text(audio_file) – Converts recorded audio to text
- get_answer(messages) – Generates chatbot responses using GPT
- text_to_speech(text) – Converts text responses to audio
- autoplay_audio(audio_file) – Plays audio in the Streamlit app

## Important Note

For security reasons, the OpenAI API key has been removed from this repository. In this project, the API key is directly set in utils.py instead of using a .env file for simplicity in running the Streamlit app. To run the app locally, clone the repository, add your OpenAI API key in the utils.py file, install the required dependencies using pip install -r requirements.txt, and run the app with (streamlit run app.py). Once running, you can interact with the voice-enabled chatbot using the microphone button to record queries and receive spoken responses.
