# llama_wrapper.py
import ollama

def run_llama(prompt: str) -> str:
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']
