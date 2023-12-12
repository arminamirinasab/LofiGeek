from django.urls import path
from .views import fetch_songs

app_name = 'main'

urlpatterns = [
    path('', fetch_songs, name='main_page'),
]