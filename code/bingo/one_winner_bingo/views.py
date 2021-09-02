from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "one_winner_bingo/index.html")

def original_bingo(request):
    return render(request, "one_winner_bingo/pages/original_bingo.html")

def custom_bingo(request):
    return render(request, "one_winner_bingo/pages/custom_bingo.html")