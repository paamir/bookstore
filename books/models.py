from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=1)
    description = models.TextField(blank=False, null=False)
    release_date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
    visibility = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=False)

    def __str__(self):
        return f'{self.author}:{self.title}'

    def get_absolute_url(self):
        return reverse('book_details', args=[self.id])


class Comment(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.name}: {self.text}'