import requests
import os

TOKEN = os.getenv
")
CHAT_ID = os.getenv

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)
  
