from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.URLField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quote} - {self.author}'

    class Meta:
        ordering = ['-added']
