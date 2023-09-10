from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'text', 'creation_datetime', 'is_recommended', 'is_active', 'comment_actions']
    actions = ['Active Selected Items', 'DeActive Selected Items']

    def comment_actions(self, obj):
        return format_html(
            '<a class="button" href="">active</a>&nbsp;'
            '<a class="button" href="">Withdraw</a>',
            # reverse('admin:account-deposit', args=[obj.pk]),
            # reverse('admin:account-withdraw', args=[obj.pk]),
        )


admin.site.register(Book)
