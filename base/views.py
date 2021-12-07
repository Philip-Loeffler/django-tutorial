from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'design with me'},
    {'id': 3, 'name': 'front end developer'},
]
# Create your views here.
# {'rooms': rooms}) Adding this allows us that room object to be accessable inside our home template
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html')