from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover_image_url = models.URLField()

    def __str__(self):
        return f'{self.title} by {self.author}'

class Comments(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.PROTECT)

    # def __str
