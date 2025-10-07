import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv("GOOGLE_API_KEY")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": api_key  
}


entree = "Quelle est la capitale de la Guinée ?"


data = {
    "contents": [
        {
            "parts": [
                {"text": entree}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
# response = Sortie


# print(response.status_code)
# print(response.json())
print(response.json()['candidates'][0]['content']['parts'][0]['text'])
