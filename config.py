TOKEN = "6433946677:AAHvXPEOgk0_C77XvpwQBbe1-oWkKlkMOzI"

from gtts import gTTS
import os

def text_to_speech(mytext, lang):
    myobj = gTTS(text=mytext, lang=lang, slow=False)
    myobj.save("audio.mp3")