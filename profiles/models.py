from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user: OneToOne binding field with Django's user model.
        favorite_city (str): Text field to save the user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Method to represent the profile as a character string.

        Returns:
            str: Username of the user associated with the profile.
        """
        return self.user.username
