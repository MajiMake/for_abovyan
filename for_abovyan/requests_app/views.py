from django.http import HttpResponse, JsonResponse
from django.db.utils import IntegrityError
import json as js
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import User
import requests

import environ
# Initialise environment variables
env = environ.Env()

PHONE_NUMBER = 'phone_number'
NAME = 'name'
TEXT = 'text'
CHAT_ID=-1001843286837

def phone_number_check(phone_number):
    if len(phone_number) > 5:
        return True
    return False

def send_telegram_update(message):
   token = env("TELEGRAM_TOKEN")
   url = f"https://api.telegram.org/bot{token}/sendMessage"
   payload = {
        "chat_id": CHAT_ID,
        "text": message,
    }
    # Send the POST request to the Telegram bot API
   response = requests.post(url, data=payload)

    # Check the response status code
   if response.status_code == 200:
        print("Message sent successfully.")
   else:
        print("Failed to send message.")


def handler(request) -> HttpResponse:
    data = js.loads(request.body)
    print(data)
    if phone_number_check(data[PHONE_NUMBER]):
        try:
            user = User(name=data[NAME], phone_number=data[PHONE_NUMBER], text=data[TEXT])
            user.save()
        except IntegrityError:
            return JsonResponse({'result': 'saving error'})
        send_telegram_update("Name: "+data[NAME]+"\nphone: "+ data[PHONE_NUMBER]+"\ntext: "+data[TEXT])
        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'result': 'not valid email'})



