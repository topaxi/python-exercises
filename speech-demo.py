# Installation
# pip install pyaudio SpeechRecognition gtts pydub

import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening... Say a command.")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an issue with the audio recognition service."

def speak(response):
    mp3_fp = BytesIO()
    tts = gTTS(text=response, lang='en')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    speech = AudioSegment.from_mp3(mp3_fp)
    play(speech)

while True:
    command = listen()

    if "hello" in command:
        response = "Hello! How can I help you?"
    elif "goodbye" in command:
        response = "Goodbye! Have a great day!"
        speak(response)
        break
    else:
        response = "I didn't catch that. Please say a valid command."

    speak(response)
