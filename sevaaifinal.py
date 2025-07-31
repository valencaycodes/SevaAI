# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 22:20:44 2025

@author: richa
"""

import sounddevice as sd
from scipy.io.wavfile import write
def record_voice(filename="user_input.wav", duration=5, fs=44100):
    print("Recording started...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)
    print("Voice recorded.")
import whisper
def speech_to_text(filename="user_input.wav"):
    model = whisper.load_model("base")
    try:
        result = model.transcribe(filename, language="hi")
        text = result.get("text", "").strip()
        if not text:
            raise ValueError("No text returned from transcription.")
        print(f"Transcribed Text: {text}")
        return text
    except Exception as e:
        print(f"ERROR in speech_to_text: {e}")
        return None
    
    print(f"Transcribed Text: {text}")
    return text
def detect_symptom(text):
    text = text.lower()
    if "बुखार" in text or "fever" in text:
        return "आपको वायरल बुखार हो सकता है। कृपया आराम करें और पानी पिएं।"
    elif "सिरदर्द" in text or "headache" in text:
        return "सिरदर्द के लिए नींद लें और दवा लें यदि आवश्यक हो।"
    elif "छाती दर्द" in text or "chest pain" in text:
        return "यह आपातकालीन लक्षण हो सकता है। कृपया तुरंत चिकित्सा सहायता लें!"
    else:
        return "मैंने आपकी लक्षणों को पूरी तरह समझा नहीं। कृपया और विवरण दें।"
def detect_emotion(text):
    text = text.lower()
    sad_words = ["दुख", "परेशान", "तनाव", "अकेला", "डर"]
    if any(word in text for word in sad_words):
        return " आप चिंतित लग रहे हैं। गहरी सांस लें, सब ठीक हो जाएगा। मैं आपके साथ हूँ।"
    return None
from gtts import gTTS
import os

def speak_response(response_text):
    tts = gTTS(text=response_text, lang="hi")
    tts.save("response.mp3")
    os.system("start response.mp3" if os.name == "nt" else "afplay response.mp3")
import datetime

def log_interaction(user_text, ai_response):
    with open("sevaai_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()}\nUser: {user_text}\nSevaAI: {ai_response}\n\n")

def run_sevaai():
    record_voice()
    user_text = speech_to_text()
    print(f"DEBUG: Transcribed text is: {user_text}")

    if not user_text:
        response_text = "माफ़ कीजिए, आपकी आवाज़ को ठीक से समझ नहीं पाया। कृपया फिर से प्रयास करें।"
        speak_response(response_text)
        log_interaction("No input", response_text)
        return

    response = detect_symptom(user_text)
    emotion = detect_emotion(user_text)
    print(f"DEBUG: Symptom: {response}, Emotion: {emotion}")

    full_response = ""
    if emotion:
        full_response += emotion + " "
    full_response += response

    speak_response(full_response)
    log_interaction(user_text, full_response)