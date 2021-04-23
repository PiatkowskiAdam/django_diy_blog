from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=5000, help_text='The title of the post')
    content = models.TextField(help_text='The contents of the post')

    def __str__(self):
        return f'"{self.title}" written by {self.author}'

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'"{self.title}" written by {self.author}'

    
    class Meta:
        ordering = ['date']


