# Installation
# pip install pyaudio SpeechRecognition gtts pydub
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import nltk
from pydub import AudioSegment
from pydub.playback import play

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening... Say a sentence.")
        audio = recognizer.listen(source)

    try:
        sentence = recognizer.recognize_google(audio)
        print(f"You said: {sentence}")
        return sentence
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

def analyze_text(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged

while True:
    sentence = listen()

    if "analyze" in sentence:
        tagged_text = analyze_text(sentence)
        response = "Here's the analysis result:"
        for word, pos in tagged_text:
            response += f" {word} ({pos}),"
        response = response.rstrip(',')  # Remove the trailing comma
    elif "goodbye" in sentence:
        response = "Goodbye! Have a great day!"
        speak(response)
        break
    else:
        response = "I didn't catch that. Please say a valid command."

    speak(response)
