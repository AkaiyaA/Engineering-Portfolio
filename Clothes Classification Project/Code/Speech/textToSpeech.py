import sys
import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import speech_recognition as sr
import pyttsx3
from outfitCreation.outfitGen import generate_outfit, group_clothes
from outfitCreation.database import get_clothes
from outfitCreation.outfitDisplay import show_outfit
from speech.aiBrain import get_ai_response

r = sr.Recognizer()
print("SpeechRecognition installed correctly")

# init TTS engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # try 0, 1, 2
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    fs = 44100
    seconds = 4

    print("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    # Convert float32 → int16 for WAV format
    recording = (recording * 32767).astype(np.int16)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, recording)

    r = sr.Recognizer()
    with sr.AudioFile(temp_file.name) as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def main_loop():
    items = get_clothes()
    wardrobe = group_clothes(items)
    
    speak("Good morning! I have some outfit ideas for you.")

    while True:
        text = listen()
        # if not text:
        #     speak("Sorry, I didn't catch that. Can you repeat?")
        #     continue

        if "REQUEST_OUTFIT" in reply:
            outfit = generate_outfit(wardrobe)
            show_outfit(outfit)
            speak("Here’s something I put together.")
        else:
            speak(reply)

        while True:
            text = listen()

            if not text:
                speak("I didn't catch that.")
                continue

            reply = get_ai_response(text)
            speak(reply)
            
if __name__ == "__main__":
    main_loop() 