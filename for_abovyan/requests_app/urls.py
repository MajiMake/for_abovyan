from django.urls import path
from .views import *

urlpatterns = [
    path('<str:json_str>', handler, name='request_json'),
]
