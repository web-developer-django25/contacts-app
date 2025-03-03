from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:contact_detail', kwargs={'pk': self.pk})
