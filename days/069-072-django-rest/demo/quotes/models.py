from django.contrib.auth.models import User
from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.URLField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return f'{self.quote} - {self.author} (submitted by {self.user})'

    class Meta:
        ordering = ['-added']
