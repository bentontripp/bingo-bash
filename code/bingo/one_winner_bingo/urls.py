from django.urls import path
from . import views

app_name = 'one_winner_bingo'

urlpatterns = [
    path('', views.bingo, name = 'bingo'),
    #path('pages/original_bingo.html', views.original_bingo),
    #path('pages/custom_bingo.html', views.custom_bingo),
    path('get_custom_bingo', views.get_custom_bingo, name='get_custom_bingo')
]