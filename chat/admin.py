from django.contrib import admin

from chat.models import Room


# Register your models here.
#관리자가 관리가능하게 설정
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass