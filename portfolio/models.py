from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
from PIL import Image
from django.core.exceptions import ValidationError


def validate_image(image):
    img = Image.open(image)
    max_image_size = (800, 800)  # Maximum allowed image size

    if img.width > max_image_size[0] or img.height > max_image_size[1]:
        raise ValidationError(
            f"Please ensure the image dimensions are within {max_image_size[0]} pixels wide and {max_image_size[1]} pixels tall."
        )


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    categories = models.ManyToManyField(Category, related_name='projects')
    tags = models.ManyToManyField(Tag, related_name='projects')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='project_images/', validators=[validate_image])
    slug = models.SlugField(max_length=200, unique=True)

    client_name = models.CharField(max_length=200)
    project_date = models.DateField()
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    skills_used = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
