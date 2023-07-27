from django.db import models

# Create your models here.

class ContactModel(models.Model):
    email = models.EmailField(max_length=50)
    message = models.TextField(default=None)

    def __str__(self):
        return self.email
    