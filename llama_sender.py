# llama_sender.py
import requests

def run_llama(prompt, model="llama3"):
    print("🧠 Sending to LLaMA...")
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    response.raise_for_status()
    content = response.json()["response"]
    print("🤖 LLaMA Response:", content)
    return content

def send(input_file="transcript.txt", output_file="response.txt"):
    with open(input_file, "r") as f:
        prompt = f.read().strip()
    reply = run_llama(prompt)
    with open(output_file, "w") as f:
        f.write(reply)
    return reply
