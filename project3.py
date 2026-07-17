import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello! I am Jarvis.")

while True:
    command = input("\nYou: ").lower()

    if command == "hello":
        speak("Hello! How are you?")

    elif command == "time":
        now = datetime.datetime.now()
        time = now.strftime("%I:%M %p")
        speak("The time is " + time)

    elif command == "google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command == "youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command == "notepad":
        speak("Opening Notepad")
        os.system("notepad")

    elif command == "bye":
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry, I don't understand.")