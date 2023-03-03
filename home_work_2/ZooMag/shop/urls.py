
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', start_page, name="start_page")
]