from django.db import models
from django.db.models.signals import post_save, post_delete
from django.urls import reverse

from app.mixins import ChannelLayerGroupSendMixin


class Post(models.Model, ChannelLayerGroupSendMixin):
    CHANNEL_LAYERS_GROUP_NAME = "liveBlog"
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['-id']


def post__on_post_save(instance: Post, created, **kwargs):
    if created:
        message_type = 'liveBlog.post.created'
    else:
        message_type = 'liveBlog.post.updated'
    post_id = instance.pk
    post_partial_url = reverse("post_partial", args=[post_id])

    instance.channel_layer_group_send({
        "type": message_type,
        "post_id": post_id,
        "post_partial_url": post_partial_url,
    })


post_save.connect(
    post__on_post_save,
    sender=Post,
    dispatch_uid="post__on_post_save",
)


def post__on_post_delete(instance: Post, **kwargs):
    post_id = instance.pk

    instance.channel_layer_group_send({
        "type": "liveBlog.post.deleted",
        "post_id": post_id,
    })


post_delete.connect(
    post__on_post_delete,
    sender=Post,
    dispatch_uid="post__on_post_delete",
)
