"""
Unit testing module for URLs of the 'profiles' application.

This module contains unit tests for the URLs of the 'profiles' application.
It checks that the URLs of profile index pages and individual profiles
are correctly configured and return the correct HTTP responses.

Note: Tests use fixtures from conftest.py to create
necessary profile instances
"""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from django.test import Client


client = Client()


@pytest.mark.django_db
def test_profiles_index_url(profile_1, profile_2):
    """
    Unit test for 'index' view URL.

    This test verifies that the URL for the 'index' view is
    correctly configured and returns the expected HTTP response.

    Args:
    profile_1 (Profile): Instance of the Profile model representing
    the first profile.
    profile_2 (Profile): Instance of the Profile model representing
    the second profile.
    """

    profile_1
    profile_2

    url = reverse('profiles:profiles_index')
    # Effectue une requete GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/profiles/'
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profiles_profile_url(profile_2):
    """
    Unit test for 'profile' view URL.

    This test verifies that the URL for the 'profile' view is
    correctly configured and returns the expected HTTP response.

    Args:
    profile_2 (Profile): Instance of the Profile model
    representing the second profile.
    """

    profile_2

    # Get URL from view
    url = reverse('profiles:profile', kwargs={"username": 'Ronald Weasley'})

    # Make GET requestEffectue une requete GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/profiles/Ronald%20Weasley/'
    assertTemplateUsed(response, "profiles/profile.html")
