from django.urls import path
from . import views

app_name = 'one_winner_bingo'

urlpatterns = [
    path('', views.bingo, name = 'bingo'),
    path('get_custom_bingo', views.get_custom_bingo, name='get_custom_bingo'),
    path('get_classic_bingo', views.get_classic_bingo, name='get_classic_bingo')
]