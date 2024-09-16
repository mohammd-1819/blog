from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('updated_at',)
    search_fields = ('title', 'body')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
