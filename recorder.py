import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper

SAMPLE_RATE = 16000
CHANNELS = 1

model = whisper.load_model("base")

def record_audio():
    print("Press Enter to start recording...")
    input()
    print("Recording... Press Enter to stop recording.")
    
    recording = []
    
    def callback(indata, frames, time, status):
        if status:
            print(status)
        recording.append(indata.copy())
    
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16', callback=callback)
    stream.start()
    input()  # wait for enter to stop
    stream.stop()
    print("Recording stopped.")
    
    audio = np.concatenate(recording, axis=0)
    write("recorded.wav", SAMPLE_RATE, audio)
    return "recorded.wav"

def transcribe(audio_path):
    print("Transcribing...")
    result = model.transcribe(audio_path)
    text = result["text"]
    print("Transcription:", text)
    with open("transcript.txt", "w") as f:
        f.write(text)
    return text

if __name__ == "__main__":
    audio_file = record_audio()
    transcribe(audio_file)
