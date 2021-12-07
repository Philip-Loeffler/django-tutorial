from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'design with me'},
#     {'id': 3, 'name': 'front end developer'},
# ]
# Create your views here.
# {'rooms': rooms}) Adding this allows us that room object to be accessable inside our home template
# def home(request):
#     context = {'rooms': rooms}
#     return render(request, 'base/home.html', context)



def home(request):
    # this is query all of the rooms in our db
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


# def room(request, pk):
#     room = None
#     for i in rooms:
#         # this is saying whatever id matches the id in the url
#         if i["id"] == int(pk):
#             room = i
#     context = {'room': room}
#     return render(request, 'base/room.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)