from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    biography = models.TextField()

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name
