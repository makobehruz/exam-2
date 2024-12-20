from django.db import models
from django.shortcuts import reverse


class Articles(models.Model):
    title = models.CharField(max_length=100)
    create_ad = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50)
    short_content = models.TextField()
    long_content = models.TextField()
    author = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'News'

    def get_detail_url(self):
        return reverse('articles:detail', args=[self.pk])