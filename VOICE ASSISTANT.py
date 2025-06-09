
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Function to make the assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the microphone
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        talk("How can I help you?")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please repeat.")
        return ""
    return command

# Function to handle commands
def run_assistant():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
    elif 'who is' in command:
        person = command.replace('who is', '')
        talk(f"Searching for {person}")
        pywhatkit.info(person, lines=2)
    elif 'exit' in command or 'stop' in command:
        talk("Goodbye!")
        exit()
    else:
        talk("I can search that for you.")
        pywhatkit.search(command)

# Run the assistant
while True:
    run_assistant()
