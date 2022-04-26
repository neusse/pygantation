import pygame
from io import BytesIO
from gtts import gTTS
import time

pygame.init()
pygame.mixer.init()
def speak(text, language='en'):
    print()
    print("Function speak has been called")
    if pygame.mixer.music.get_busy():
        print("-----")
        print("mixer busy")
        print("try again")
        pygame.mixer.music.unload()
        time.sleep(.3)
        speak(text, language)
    else:
        print("Mixer is at disposal")
        mp3_fo = BytesIO()
        try:
            tts = gTTS(text, lang=language)
            print("gTTS working")
        except Exception:
            print("Internet may be slow")
        tts.write_to_fp(mp3_fo)
        pygame.mixer.music.unload()
        print(text)
        x = pygame.mixer.music.load(mp3_fo, 'mp3')
        pygame.mixer.music.play()
# Button 1 istance