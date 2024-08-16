from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from chat.forms import RoomForm
from chat.models import Room
from hashids import Hashids


# TODO:채팅방 삭제에서 문제가 생겨서 일단 주석처리
#hashids = Hashids(salt='thismysalt', min_length=4)


# Create your views here.
@login_required
def index(request):
    room_list = Room.objects.all()
    return render(request, "chat/index.html", {'room_list': room_list})


@login_required
def room_chat(request, room_pk: str):
    #if room_pk.isdecimal():
    #    return redirect("chat:room_chat", room_pk)
    #room_pk = hashids.decode(room_pk)[0];
    room = get_object_or_404(Room, pk=room_pk)
    return render(request, "chat/room_chat.html", {
        "room_name": room.name,
        "room_owner": room.owner,
        "room_pk": room_pk
    })


@login_required
def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            #커밋 헤제하고
            created_room = form.save(commit=False)
            #유저값 넣은뒤
            created_room.owner = request.user
            # 커밋
            created_room.save()
            #room_pk = hashids.encode(created_room.pk)
            return redirect("chat:room_chat", created_room.pk)
    else:
        form = RoomForm
    return render(request, "chat/room_form.html", {"form": form})


@login_required
def room_delete(request, room_pk: str):
    #room_pk = hashids.decode(room_pk)[0]
    room = get_object_or_404(Room, pk=room_pk)

    # 근데 이거는 프런트쪽에서 해도 되지않을까 싶다
    if room.owner != request.user:
        messages.error(request, "채팅방 소유자가 아닙니다")
        return redirect("chat:index")

    if request.method == "POST":
        room.delete()
        messages.success(request, "채팅방 삭제완료")
        return redirect("chat:index", )

    return render(request, "chat/room_confirm_delete.html", {"room": room})
