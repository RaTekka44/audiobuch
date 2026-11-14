from gtts import gTTS

with open("beispiel.txt", "r") as file:
    text = file.read()

audio = gTTS(text=text, lang="de")
audio.save("audiobuch.mp3")