from django.db import models
from django.utils.text import slugify


class Language(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=50)
    
    text = models.TextField()
    text_language = models.ForeignKey(Language, related_name='language_text',
        on_delete=models.DO_NOTHING)

    translation = models.TextField()
    translation_language = models.ForeignKey(Language,
        related_name='language_translation',
        on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.translation:
            return self.translation[:50]
        return self.text[:50]


class Statistic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    used_times = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.post)
