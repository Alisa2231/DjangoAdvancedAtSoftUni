from django.db import models
#
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=0)
    description = models.TextField(max_length=100, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    # author = models.CharField(max_length=100)