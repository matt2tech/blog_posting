from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    cover_image_url = models.URLField()

    def __str__(self):
        return f'{self.title} by {self.author}'

    @staticmethod
    def submitted(title, body, author, cover_image):
        BlogPost(title=title, body=body, author=author, cover_image_url=cover_image).save()

class Comments(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
