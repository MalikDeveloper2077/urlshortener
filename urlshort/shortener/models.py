from django.db import models


class URL(models.Model):
    """Shortened URL"""
    original_url = models.URLField(null=False)
    short_url = models.CharField(max_length=20, unique=True, blank=True)
    follow_count = models.PositiveIntegerField('Переходов', default=0)

    def __str__(self):
        return f'{self.original_url} - {self.short_url}'
