from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Accommodate hashed passwords

    def __str__(self):
        return self.name