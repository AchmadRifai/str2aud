from gtts import gTTS
mytext = "Selamat datang di PT Andara Rejo Makmur"
audio = gTTS(text=mytext, lang="id", slow=True)
audio.save("example.mp3")
