from django.db import models
from django.urls import reverse

# Category model
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


# Tag model
class Tag(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

# Post model

class Post(models.Model):
    title = models.CharField(max_length=255, )
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name="Количество просмотров")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
