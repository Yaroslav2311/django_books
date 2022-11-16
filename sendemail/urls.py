from django.urls import path

from .views import create_form

app_name = 'sendemail'
urlpatterns = [
    path('', create_form, name='create_form'),
]
