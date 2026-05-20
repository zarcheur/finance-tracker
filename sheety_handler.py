import requests
from datetime import datetime
import os

TOKEN = os.environ.get("TOKEN")
PROJECT_NAME = os.environ.get("PROJECT_NAME")
SHEET_NAME = os.environ.get("SHEET_NAME")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

SHEETY_ENDPOINT = f"https://api.sheety.co/{TOKEN}/{PROJECT_NAME}/{SHEET_NAME}"
HEADER = {"Authorization": f"Basic {os.environ.get('AUTH_TOKEN')}"}

def post_to_sheety(parsed_data):
    today = datetime.now().strftime("%d/%m/%Y")

    amount = parsed_data["amount"]
    if parsed_data["type"] == "expense":
        amount = -amount

    payload = {
        SHEET_NAME: {
            "date": today,
            "type": parsed_data["type"],
            "amount": amount,
            "category": parsed_data["category"],
            "description": parsed_data["description"]
        }
    }

    response = requests.post(SHEETY_ENDPOINT, json=payload, headers=HEADER)

    if response.status_code == 200:
        print(f"✅ Successfully logged: {parsed_data['description']}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

    return response.json()