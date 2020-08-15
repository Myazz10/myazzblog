from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# -->> This was installed python -m pip install django-multiselectfield to use the multiselectfield
# Now I must install it in my apps in the settings.py as 'multiselectfield'
from multiselectfield import MultiSelectField
from django import forms
from django.urls import reverse
from django.db.models import Count


# PLEASE REMEMBER TO MAKE A CLASS MODEL TO RECORD THE AMOUNT OF VISITORS THAT VISITS THE SITE OKAY...


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Travel', 'Travel'),
        ('Fashion', 'Fashion'),
        ('Technology', 'Technology'),
        ('Food', 'Food'),
        ('Photography', 'Photography')
    )
    OTHER_CHOICES = (
        ('random', 'Random'),
        ('nice', 'Nice'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    intro_content = models.TextField(null=True)
    intro_picture = models.ImageField(
        upload_to='blog_post_images', default='default.jpg')
    content = models.TextField(null=True)
    picture = models.ImageField(
        upload_to='blog_post_images', default='default.jpg')
    #category_tags = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    category_tags = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='category')
    soft_tags = MultiSelectField(choices=OTHER_CHOICES, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    hyperlink = models.URLField(null=True)

    # To check the amount of views the post received...
    # Editable will remove the option to edit if from the admin section...
    view_count = models.PositiveIntegerField(default=0, editable=False)

    @property
    def category_count(self):
        return Post.objects.values('category_tags').annotate(Count('category_tags')).order_by()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.intro_picture.path)

        if img.height > 800 and img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.intro_picture.path)

    def __str__(self):
        return f'{self.title.title()} - {self.author.first_name} {self.author.last_name}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    reply = models.ForeignKey(
        'self', null=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']  # To put the latest comment on top

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return f'{self.author.title()}'


class Popular_Article(models.Model):
    popular_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, related_name='popular_posts')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.popular_post}'
