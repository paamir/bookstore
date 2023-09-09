from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=1)
    description = models.TextField(blank=False, null=False)
    release_date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}:{self.title}'

    def get_absolute_url(self):
        return reverse('book_details', args=[self.id])
