import os
import base64          # For encoding audio to base64 in autoplay_audio
import openai
from openai import OpenAI  # For client initialization
from dotenv import load_dotenv
import streamlit as st     # For Streamlit frontend display


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)

def get_answer(messages):
    system_message = [{"role": "system", "content": "You are an AI Chatbot, that answers questions asked by User"}]
    messages=system_message + messages
    response=client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    return response.choices[0].message.content

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript=client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
    return transcript.text

def text_to_speech(input_text):
    mp3_file_path = "temp_audio_play.mp3"
    
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",   # or "tts-1"
        voice="nova",
        input=input_text,
    ) as response:
        response.stream_to_file(mp3_file_path)

    return mp3_file_path

def autoplay_audio(file_path:str):
    with open(file_path, "rb") as f:
        data=f.read()
    b64=base64.b64encode(data).decode()
    md=f"""
    <audio autoplay="true" controls="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)