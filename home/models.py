from django.db import models

# Create your models here.

# Model for contact us
class Contact(models.Model):
    name        =   models.CharField(max_length=100)
    subject     =   models.CharField(max_length=100)
    email       =   models.CharField(max_length=100)
    message     =   models.TextField()
    created_at  =   models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + "(" +self.email + ")"
    