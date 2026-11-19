
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# Listen to microphone
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=7
            )
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You:", command)
            return command

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
            return ""

        except sr.RequestError:
            speak("Internet connection problem.")
            return ""

# Process voice commands
def run_assistant(command):

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "your name" in command:
        speak("My name is Jarvis, your Python voice assistant.")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad.exe")

    elif "search" in command:
        query = command.replace("search", "", 1).strip()
        if query:
            speak("Searching Google for " + query)
            webbrowser.open(
                "https://www.google.com/search?q=" + query.replace(" ", "+")
            )

    elif "stop" in command or "exit" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, this command is not available yet.")

    return True

# Main program
def main():
    speak("Hello! I am Jarvis. Your voice assistant is ready.")

    running = True

    while running:
        command = listen()

        if command:
            running = run_assistant(command)

if __name__ == "__main__":
    main()
