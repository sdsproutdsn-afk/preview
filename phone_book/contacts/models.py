from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name