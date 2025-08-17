import requests
import os

TOKEN = os.getenv("8471294862:AAG1ixrA0GMCF4fhqwRPlDhqV7tFFXhqoS4
")
CHAT_ID = os.getenv("6300358705")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_message("✅ Bot ya fara aiki lafiya!")
  
