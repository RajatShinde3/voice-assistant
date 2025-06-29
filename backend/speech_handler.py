# backend/speech_handler.py

import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen() -> str:
    """Capture voice input from microphone and return it as text."""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."

def speak(text: str, filename: str = "response.mp3") -> str:
    """Convert text to speech and save it as an audio file."""
    try:
        print(f"🗣️ Speaking: {text}")
        tts_engine.save_to_file(text, filename)
        tts_engine.runAndWait()
        return filename
    except Exception as e:
        print(f"❌ Error in speak(): {e}")
        return ""
