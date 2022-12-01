from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

'''
rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'Front end devs'},
    {'id':3, 'name':'Design'}
] '''

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def create_room(request):

    context = {}
    return render(request, 'base/room_form.html', context)