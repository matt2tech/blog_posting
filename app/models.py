from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover_image_url = models.TextField()

class Comments(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    blog_post = models.ForeignKey(BlogPost)
