from django.contrib import admin

from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'text', 'creation_datetime']


admin.site.register(Book)

    