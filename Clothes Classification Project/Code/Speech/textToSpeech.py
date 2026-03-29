
import sys
import os

# from matplotlib import text
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import speech_recognition as sr
import pyttsx3
from outfit.outfitGen import generate_outfit, group_clothes
from outfit.database import get_clothes
from outfit.outfitDisplay import show_outfit_fullscreen
from speech.aiBrain import get_ai_response

from pathlib import Path

import time

is_speaking = False

env_path = Path(__file__).resolve().parents[1] / ".env"

r = sr.Recognizer()
# print("SpeechRecognition installed correctly") --- IGNORE ---



# init TTS engine
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[41].id) #change or sum
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)

is_speaking = False

# def speak(text):
#     global is_speaking
#     is_speaking = True

def speak(text):
    global is_speaking
    is_speaking = True

    print("SPEAKING:", text)

    try:
        import pyttsx3
        import sounddevice as sd
        import soundfile as sf
        import tempfile
        import os
        import re

        # Split into sentences (handles ., !, ?)
        sentences = re.split(r'(?<=[.!?]) +', text)

        for sentence in sentences:
            if not sentence.strip():
                continue

            with tempfile.NamedTemporaryFile(delete=False, suffix=".aiff") as fp:
                temp_path = fp.name

            engine = pyttsx3.init(driverName='nsss')
            engine.setProperty('rate', 200)
            engine.setProperty('volume', 1.0)

            engine.save_to_file(sentence, temp_path)
            engine.runAndWait()
            engine.stop()

            data, samplerate = sf.read(temp_path)
            sd.play(data, samplerate)
            sd.wait()

            os.remove(temp_path)

            time.sleep(0.1)  # tiny pause between sentences

    except Exception as e:
        print("TTS ERROR:", e)

    is_speaking = False

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            return ""

    try:
        return r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
    
# reply = "hello human"

def safe_show_outfit_fullscreen(outfit):
    show_outfit_fullscreen(outfit)

# def speak_and_wait(text):
#     global is_speaking
#     is_speaking = True

#     engine.say(text)
#     engine.runAndWait()

#     time.sleep(0.3)

#     is_speaking = False

def main_loop():
    items = get_clothes()
    wardrobe = group_clothes(items)

    speak("Good morning! I have some outfit ideas for you.")

    while True:
        while is_speaking:
            time.sleep(0.05)

        text = listen()

        if not text:
            continue

         # dismissal phrases
        dismiss_phrases = ["thank you", "thanks", "bye", "that’s all", "thats all", "exit", "quit"]

        if any(phrase in text for phrase in dismiss_phrases):   
            speak("You're welcome. Have a great day.")
            break

        reply = get_ai_response(text)
        # reply = "hello human"

        if "REQUEST_OUTFIT" in reply:
            speak("Sure thing. Give me a second.")

            outfit = generate_outfit(wardrobe)
            safe_show_outfit_fullscreen(outfit)

            speak("Here’s what I picked for you.")
        else:
            speak(reply)

        # if "hey closet" in text:
        #     speak("Yeah?")
            
if __name__ == "__main__":
    main_loop() 