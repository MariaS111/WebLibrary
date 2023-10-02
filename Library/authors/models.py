from django.core.validators import MinValueValidator
from django.db import models
from datetime import date
from django.urls import reverse


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        validators=[MinValueValidator(limit_value=date(1, 1, 1))])
    biography = models.TextField(max_length=600)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('author', kwargs={'pk': self.pk})
