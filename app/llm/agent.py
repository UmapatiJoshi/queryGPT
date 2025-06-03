# app/llm/agent.py

import requests
from app.config import OLLAMA_CONFIG

def query_ollama(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_CONFIG['base_url']}/api/generate",
        json={
            "model": OLLAMA_CONFIG['model'],
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        raise Exception(f"Ollama error: {response.status_code} - {response.text}")
