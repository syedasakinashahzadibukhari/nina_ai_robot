import pyttsx3

# Initialize engine once
engine = pyttsx3.init()

# Optional: set properties
voices = engine.getProperty('voices')  # List all voices
engine.setProperty('voice', voices[1].id)  # Change index to select male/female
engine.setProperty('rate', 150)          # Speed of speech (default ~200)
engine.setProperty('volume', 1.0)        # Volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()