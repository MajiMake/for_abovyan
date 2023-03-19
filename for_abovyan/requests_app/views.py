from django.http import HttpResponse, JsonResponse
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


def handler(request) -> HttpResponse:
    data = js.loads(request.body)
    print(data)
    if email_check(data['email']):
        try:
            user = User(name=data['name'], email=data['email'], text=data['text'])
            user.save()
        except IntegrityError:
            return JsonResponse({'result': 'saving error'})
        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'result': 'not valid email'})



