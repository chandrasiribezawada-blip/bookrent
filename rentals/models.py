from django.db import models
from django.conf import settings
from books.models import Book


class RentalRequest(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('RETURNED', 'Returned'),
    ]

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    request_date = models.DateTimeField(
        auto_now_add=True
    )

    return_date = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.book.title} - {self.borrower.username}"