from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get("searchMovie")
    movies = Movie.objects.filter(title__icontains=searchTerm) if searchTerm else Movie.objects.all()
    ctxt = {"movies": movies, "searchTerm":searchTerm}
    for movie in movies:
        print(movie.image.url)
    return render(request, "index.html", ctxt)

def about(request):
    return render(request, 'about.html')

