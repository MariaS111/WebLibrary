from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('authors.Author', on_delete=models.RESTRICT)
    publication_year = models.IntegerField(
        validators=[MinValueValidator(limit_value=1)])
    description = models.TextField(max_length=500)
    cover = models.ImageField(upload_to='books/', default='books/book-icon.jpg')
    average_rating = models.FloatField(default=0)
    date_of_publication = models.DateField(auto_now_add=True)
    date_of_update = models.DateField(auto_now=True)

    def update_average_rating(self):
        ratings = BookRating.objects.filter(book=self)
        if ratings.exists():
            total_ratings = ratings.aggregate(models.Sum('rating'))['rating__sum']
            count_ratings = ratings.count()
            self.average_rating = total_ratings / count_ratings
            self.save()
        else:
            self.average_rating = 0
            self.save()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-date_of_update']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': self.pk})


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_average_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.book.update_average_rating()


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date_of_publication = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['date_of_publication']

    def __str__(self):
        return self.book.title + str(self.pk)


