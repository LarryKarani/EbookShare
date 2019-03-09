from django.db import models

class User(models.Model):
    """
    User Model
    Defines the attributes of a User
    """
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def get_email(self):
        return self.email

    def __repr__(self):
        return self.username

