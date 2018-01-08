from django.db import models
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=120)
    content= models.TextField()
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title

    def absolute_url(self):
        return reverse('posts:details',kwargs={'id':self.id})