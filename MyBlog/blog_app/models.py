from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.CharField(max_length=100, default='Some')
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return self.title