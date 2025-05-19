# main.py
from recorder import record_audio, transcribe
from llama_sender import send
from speaker import speak_text

if __name__ == "__main__":
    print("🟢 Voice Assistant Started.")
    while True:
        try:
            audio_path = record_audio()          # Wait for Enter, record, wait for Enter to stop
            text = transcribe(audio_path)        # Transcribe recorded audio
            
            if not text.strip():
                continue
            
            response = send()                    # send() reads transcript.txt internally
            speak_text(response)
        except KeyboardInterrupt:
            print("\n👋 Exiting.")
            break
