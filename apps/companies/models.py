from django.conf import settings
from django.db import models


class Company(models.Model):
    CURRENCIES = [
        ("UGX", "Ugandan Shilling"),
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
        ("KES", "Kenyan Shilling"),
        ("TZS", "Tanzanian Shilling"),
    ]

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="company",
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    currency = models.CharField(
        max_length=10, choices=CURRENCIES, default="UGX"
    )
    tax_number = models.CharField(max_length=100, blank=True)
    footer = models.TextField(blank=True)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    watermark = models.ImageField(upload_to="watermarks/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
