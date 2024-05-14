"""
Unit testing module for the Profile model of the 'profiles' application.

This module contains unit tests for the Profile model of the 'profiles'
application.
It checks the behavior of model methods and attributes, with emphasis on
the __str__ method which generates a textual representation of the profile.
"""

import pytest
from django.test import Client
from profiles.models import Profile


client = Client()


@pytest.mark.django_db
def test_profile_model(user_1):
    """
    Unit test for the Profile model.

    This test verifies that the __str__ method of the Profile model
    generates the representation expected for a profile instance
    with an associated user.

    Args:
    user_1 (User): Instance of the User model representing the first user.
    """
    # Creates a profile with the specified user and a preferred city
    profile = Profile.objects.create(user=user_1, favorite_city='Préaulard')
    assert str(profile) == "Harry Potter"
