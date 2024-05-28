from django.contrib import admin
from .models import Category, Post
from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(Category)
# class CategoryAdmin(DraggableMPTTAdmin):
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post)