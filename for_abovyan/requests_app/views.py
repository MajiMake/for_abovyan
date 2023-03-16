from django.http import HttpResponse
from django.db.utils import IntegrityError
import json as js
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import User


def email_check(email):

    try:
        validate_email(email)
    except ValidationError as e:
        return False
    else:
        return True


def name_check(name):
    symbols = ('.', ',', ':', ';','<', '>', '?', '"', "'", '[',']', '{', '}', '!','@', '#', '$', '%', "^", '&',
               '*', '(', ')', '-', '=', '_', '+', "/", '\\',
               )
    try:
        name, family_name = name.split(' ')
        for word in name:
            if word in symbols:
                return False
        for word in family_name:
            if word in symbols:
                return False

        return True

    except Exception:

        return False




def handler(request, json_str: str) -> HttpResponse:
    data = js.loads(json_str)
    if email_check(data['email']):
        if name_check(data['name']):
            try:
                user = User(name=data['name'], email=data['email'], text=data['text'])
                user.save()
            except IntegrityError:
                return HttpResponse('Email уже занят')
            return HttpResponse('Все четко')

    return HttpResponse('НЕ ЧЕТКО')



