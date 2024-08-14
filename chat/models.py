from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)

    @property
    def chat_group_names(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)

    class Meta:
        # 디폴트 정렬옵션 적용 위해 사용
        ordering = ['-pk']
