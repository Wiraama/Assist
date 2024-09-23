import pyttsx3

engine = pyttsx3.init()

def announce_words(words):
    engine.say(words)
    engine.runAndWait()
print("talking...")
announce_words("Hello, this is Python Code")
print("done...")
