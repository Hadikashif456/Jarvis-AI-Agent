import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Speak clearly.")

        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        command = recognizer.recognize_google(audio)  # Convert speech to text
        print(f"🔹 Recognized: {command}")  # ✅ Debugging step
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError:
        print("❌ Could not connect to Google Speech API. Check internet.")
        return ""
import pyttsx3

def speak(text):
    engine = pyttsx3.init()  # Initialize text-to-speech engine
    engine.say(text)
    engine.runAndWait()
