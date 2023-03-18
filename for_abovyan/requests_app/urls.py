from django.urls import path
from .views import *

urlpatterns = [
    path('', handler, name='request_json'),
]
