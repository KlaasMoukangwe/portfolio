from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='post_images/')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_excerpt(self):
        return self.content[:200] + '...'  # Extract a short excerpt of the content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
