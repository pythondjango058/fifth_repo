from django.shortcuts import render
from forms import AddMovies
from testapp.models import Movies

# Create your views here.
def indexview(request):
    return render(request, 'testapp/index.html')

def addmovies(request):
    addmovie=AddMovies()
    if request.method=='POST':
        addmovie=AddMovies(request.POST)
        if addmovie.is_valid():
            addmovie.save(commit=True)
            print('user data submitted successfully in the database')
        return indexview(request)
    return render(request,'testapp/addmovies.html',{'addmovie':addmovie})

def listmovie(request):
    list=Movies.objects.all()
    return render(request,'testapp/movieslist.html',{'list':list})
