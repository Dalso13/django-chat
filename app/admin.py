from django.contrib import admin
from django.db import models

from app.models import Post


# Create your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
# Register your models here.
