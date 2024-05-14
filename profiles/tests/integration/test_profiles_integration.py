"""
Integration testing module for the 'profiles' application.

This module contains an integration test that checks the behavior of views
of the 'profiles' application. The test verifies that the profile index pages
and individual profile pages are accessible and contain the information
expected for two specific profiles.
"""

import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()


@pytest.mark.django_db
def test_profiles_integration(profile_1, profile_2):
    """
    Integration test for views of the 'profiles' application.

    This test checks the behavior of the 'profiles' application views.
    It esures that the profile index page and individual profile page
    are accessible and contain the expected information for
    two specific profiles.

    Args:
    profile_1 (Profile): Instance of the Profile model representing
    the first profile.
    profile_2 (Profile): Instance of the Profile model representing
    the second profile.
    """

    # Testing the profile index page
    url = reverse("profiles:profiles_index")
    response = client.get(url)
    content = response.content.decode()

    assert 'Harry Potter' in content
    assert 'Ronald Weasley' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")

    # Testing the profile page for the first user (Harry Potter)
    url_2 = reverse("profiles:profile", kwargs={"username": "Harry Potter"})
    response = client.get(url_2)
    content = response.content.decode()

    expected_content = profile_1.favorite_city

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")

    # Testing the profile page for the escond user (Ronald Weasley)
    url_3 = reverse("profiles:profile", kwargs={"username": "Ronald Weasley"})
    response = client.get(url_3)
    content = response.content.decode()

    expected_content = profile_2.favorite_city

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
