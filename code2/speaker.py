from io import BytesIO
import pygame
import tkinter as tk
from gtts import gTTS
from code.label import *
from code.initialization import *
import time


pygame.init()
pygame.mixer.init()
def speak(text, language='en'):
    global tms

    if pygame.mixer.music.get_busy():
        speak(text)

    print(text)
    Label(
        screen,
        text=text, 
        position=(10, 200),
        size=60,
        color="white")
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    pygame.mixer.music.unload()
    pygame.mixer.music.load(mp3_fo, 'mp3')
    tms = mp3_fo.getbuffer().nbytes/5000 # time to speak sentence
    pygame.mixer.music.play()
    return tms

def speaktime(text, language='en'):
    global tms
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    # x = pygame.mixer.music.load(mp3_fo, 'mp3')
    tms = mp3_fo.getbuffer().nbytes/500 # time to speak sentence
    # pygame.mixer.music.play()
    return tms




if __name__ == '__main__':
    root = tk.Tk()

    tx = tk.Text(root)
    tx.pack()
    bt = tk.Button(root, text="PLAY",
        command=lambda: speak(tx.get('0.0', tk.END)))
    bt.pack()
    root.mainloop()