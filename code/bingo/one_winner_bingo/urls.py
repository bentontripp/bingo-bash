from django.urls import path
from . import views

app_name = 'one_winner_bingo'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pages/original_bingo.html', views.original_bingo),
    path('pages/custom_bingo.html', views.custom_bingo)
]