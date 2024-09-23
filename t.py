from gtts import gTTS
import os

def announce_words(words):
    tts = gTTS(text=words, lang='en')
    tts.save("output.mp3")
    os.system("mpv output.mp3")  # You may need to install `mpv` with `pkg install mpv`

print("talking...")
announce_words("Hello, this is Python Code")
print("done...")

