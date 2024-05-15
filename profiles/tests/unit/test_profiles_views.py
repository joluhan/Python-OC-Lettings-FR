"""
Unit testing module for views of the 'profiles' application.

This module contains unit tests for views of the 'profiles' application.
It checks that the 'index' and 'profile' views return the expected
HTTP responses and contain the correct profile information.

Note: Tests use fixtures from conftest.py to create
necessary profile instances
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_profiles_index_view(profile_1, profile_2):
    """
    Unit test for the 'index' view.

    This test verifies that the 'index' view returns the expected
    HTTP response and contains the expected profile information.

    Args:
    profile_1 (Profile): Instance of the Profile model representing
    the first profile.
    profile_2 (Profile): Instance of the Profile model representing
    the second profile.
    """

    # Create two profiles using fixtures
    profile_1
    profile_2

    # Gets URL path from view
    path = reverse("profiles:profiles_index")

    # Make a GET request
    response = client.get(path)
    content = response.content.decode()

    # Verifies that links to profiles are present in the content
    expected_content_1 = (
        '<a href="/profiles/Harry%20Potter/">Harry Potter</a>'
        )
    expctd_contnt_2 = (
        '<a href="/profiles/Ronald%20Weasley/">Ronald Weasley</a>'
    )
    assert expected_content_1 in content and expctd_contnt_2 in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_profile_view(profile_2):
    """
    Unit test for the 'profile' view.

    This test verifies that the 'profile' view returns the expected
    HTTP response and contains the expected profile information.

    Args:
    profile_2 (Profile): Instance of the Profile model representing
    the second profile.
    """

    # Use the fixture to create a profile
    profile_2

    # Gets URL path from view
    path = reverse("profiles:profile", kwargs={'username': "Ronald Weasley"})

    # Make a GET request
    response = client.get(path)
    content = response.content.decode()

    assert 'Le Terrier' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
