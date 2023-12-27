import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . .")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing. . .")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    if "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"The current date is {current_date}")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "open google" in command:
        speak("Opening Google sir...")
        webbrowser.open("https://www.google.com")
    elif "open notepad" in command:
        speak("Opening Notepad sir...")
        os.system("notepad")
    elif "open spotify" in command:
        speak("Opening spotify sir...")
        os.system("Spotify")
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm Naruto Uzumaki. How can I assist you today?")

    while True:
        command = listen()
        if command:
            execute_command(command)
