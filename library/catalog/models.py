from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="введите жанр книги")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="введите описание")
    isbn = models.CharField('ISBN', max_length=13, help_text="введите ISBN")
    genre = models.ManyToManyField(Genre, help_text="выберите жанр")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="уникальный номер")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = [

    ]
