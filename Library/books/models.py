from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('authors.Author', on_delete=models.DO_NOTHING)
    publication_year = models.IntegerField(
        validators=[MinValueValidator(limit_value=1)])
    description = models.TextField(max_length=500)
    cover = models.ImageField(upload_to='books/', default='books/book-icon.jpg')
    date_of_publication = models.DateField(auto_now_add=True)
    date_of_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-date_of_update']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': self.pk})


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=200)
    date_of_publication = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['date_of_publication']

    def __str__(self):
        return self.book.title + str(self.pk)


