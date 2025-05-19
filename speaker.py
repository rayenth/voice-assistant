# speaker.py
import pyttsx3
import threading
import sounddevice as sd
import numpy as np

engine = pyttsx3.init()
engine.setProperty('rate', 170)

interrupted = False

def is_speaking():
    return engine._inLoop

def monitor_interrupt(threshold=0.02, duration=0.2):
    global interrupted
    while not interrupted:
        chunk = sd.rec(int(duration * 16000), samplerate=16000, channels=1, dtype='float32')
        sd.wait()
        if np.abs(chunk).mean() > threshold:
            interrupted = True
            engine.stop()
            print("🛑 Speaking interrupted by user.")
            break

def speak_text(text):
    global interrupted
    interrupted = False
    thread = threading.Thread(target=monitor_interrupt)
    thread.start()
    engine.say(text)
    engine.runAndWait()
