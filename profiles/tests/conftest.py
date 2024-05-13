"""
Fixtures module for testing the 'profiles' application.

This module contains fixtures necessary for testing the 'profiles' application.
It defines preparatory data, such as users and profiles, for
facilitate the creation of necessary instances during unit
and integration testing.
"""

import pytest
from profiles.models import Profile


# Fixture for user 1
@pytest.fixture
def user_1(django_user_model):
    """
    Fixture to create a user (Harry Potter) to use in testing.

     Args:
        django_user_model: Django user model.

     Returns:
        User: Instance of the user model for Harry Potter.
    """
    user = django_user_model.objects.create(
        username='Harry Potter', password='quidditch')
    return user


# Fixture for user 2
@pytest.fixture
def user_2(django_user_model):
    """
    Fixture to create a user (Ronald Weasley) to use in testing.

    Args:
    django_user_model: Django user model.

    Returns:
    User: User model instance for Ronald Weasley.
    """
    user = django_user_model.objects.create(
        username='Ronald Weasley', password='hermoine4ever'
    )
    return user


# Fixture for user profile 1
@pytest.fixture
def profile_1(user_1):
    """
    Fixture to create a profile (Préaulard) linked to user 1 for testing.

    Args:
    user_1: User 1 instance.

    Returns:
    Profile: Instance of the profile template for Hogwarts.
    """
    profile = Profile.objects.create(user=user_1, favorite_city='Préaulard')
    return profile


# Fixture for user profile 2
@pytest.fixture
def profile_2(user_2):
    """
    Fixture to create a profile (Le Terrier) linked to user 2 for testing.

    Args:
    user_2: User 2 instance.

    Returns:
    Profile: Instance of the profile template for Le Terrier.
    """
    profile = Profile.objects.create(user=user_2, favorite_city='Le Terrier')
    return profile
