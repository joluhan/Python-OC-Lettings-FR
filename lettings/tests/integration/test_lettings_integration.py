"""
Integration testing module for the 'lettings' application.

This module contains integration tests simulating the user journey through
views of the 'lettings' application. It checks that the pages are correctly
rendered with the expected information.
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()


@pytest.mark.django_db
def test_lettings_integration(letting_1, letting_2):
    """
    Integration test for 'lettings' application views.

    This test simulates the user journey through the views of the 'lettings'
    application and verifies that the pages are correctly rendered with
    the expected information.
    """

    # Data preparation with two Letting objects
    letting_1
    letting_2

    # Retrieving the URL via the 'lettings_index' view
    url = reverse("lettings:lettings_index")
    response = client.get(url)
    content = response.content.decode()

    # Checking the contents of the index page
    assert "The Burrow" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")

    # Test display of letting_1 with the 'letting' URL
    url_2 = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(url_2)
    content = response.content.decode()

    # Checking the contents of the details page for letting_1
    assert "Privet Drive" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")

    # Test display of letting_2 with the 'letting' URL
    url_3 = reverse("lettings:letting", kwargs={"letting_id": 2})
    response = client.get(url_3)
    content = response.content.decode()

    # Checking the contents of the details page for letting_2
    assert "Square Grimmaurd" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
