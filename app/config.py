# app/config.py

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "ecommerce_demo",
    "port": 3306
}

OLLAMA_CONFIG = {
    "model": "mistral",  # already installed via Ollama
    "base_url": "http://localhost:11434"
}
