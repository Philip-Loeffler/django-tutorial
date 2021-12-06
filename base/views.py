from django.shortcuts import render
from django.http import HttpResponse


rooms = {
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'design with me'},
    {'id': 3, 'name': 'front end developer'},
}
# Create your views here.
# {'rooms': rooms}) Adding this allows us that room object to be accessable inside our home template
def home(request):
    # can also do it like this
    # context = {'rooms': rooms}
    # then pass context into the render function
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')