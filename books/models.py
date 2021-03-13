from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=64, default="<no author>")
    pages = models.IntegerField()
    fiction_or_non = models.BooleanField()

    def __str__(self):
        return f"ID: {self.id} Title: {self.title}"
