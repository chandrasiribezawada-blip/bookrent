from django.db import models
from django.conf import settings


class Book(models.Model):

    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Programming', 'Programming'),
        ('Science', 'Science'),
        ('Other', 'Other'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='books/',
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title