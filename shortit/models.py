from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=10, unique=True)

    def get_absolute_url(self):
        return f'/{self.short_id}'
