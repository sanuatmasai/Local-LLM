import requests

# Your local Ollama server URL
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Define the prompt
prompt = "What is the capital of France?"

# Create the payload
payload = {
    "model": "tinyllama",  # Change to "mistral", "llama3", etc. if needed
    "prompt": prompt,
    "stream": False
}

# Send request to Ollama's local API
response = requests.post(OLLAMA_API_URL, json=payload)

# Parse the response
if response.status_code == 200:
    result = response.json()
    print(f"\n🟡 Prompt: {prompt}")
    print(f"🧠 AI Response: {result['response'].strip()}")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
