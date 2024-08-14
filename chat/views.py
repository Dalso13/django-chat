from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from chat.forms import RoomForm
from chat.models import Room
from hashids import Hashids

hashids = Hashids(salt='thismysalt', min_length=4)


# Create your views here.
@login_required
def index(request):
    room_list = Room.objects.all()
    return render(request, "chat/index.html", {'room_list': room_list})


@login_required
def room_chat(request, room_pk: str):
    if room_pk.isdecimal():
        return redirect("chat:room_chat", hashids.encode(int(room_pk)))
    room = get_object_or_404(Room, pk=hashids.decode(room_pk)[0])
    return render(request, "chat/room_chat.html", {
        "room_name": room.name,
    })


@login_required
def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            created_room = form.save()
            return redirect("chat:room_chat", hashids.encode(created_room.pk))
    else:
        form = RoomForm
    return render(request, "chat/room_form.html", {"form": form})
