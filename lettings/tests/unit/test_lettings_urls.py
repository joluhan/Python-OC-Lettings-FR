"""
Unit testing module for URLs of the 'lettings' application.

This module contains unit tests for 'lettings' application URLs, including
the 'index' and 'letting' views. Tests verify that URLs return responses
HTTP 200 with the appropriate templates.
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting


# Instantiating the test client
client = Client()


# Test for view URL 'lettings_index'
@pytest.mark.django_db
def test_lettings_index_url(address_1, address_2):
    """
    Unit test for URL of 'index' view of 'lettings' application.

    This test creates instances of Letting models and verifies that
    the view URL 'index' returns an HTTP 200 response and uses the
    'lettings/index.html' template.
    """

    # Creating Letting model instances with specific addresses
    Letting.objects.create(title="Harry Potter's House", address=address_1)
    Letting.objects.create(title="The Burrow", address=address_2)

    # Get URL from view
    url = reverse('lettings:lettings_index')
    # Perform a GET request
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/lettings/'
    assertTemplateUsed(response, "lettings/index.html")


# Test for the URL of the 'letting' view
@pytest.mark.django_db
def test_lettings_letting_url(address_2):
    """
    Unit test for the URL of the 'letting' view of the 'lettings' application.

    This test creates a Letting model instance and checks
    that the URL of the 'letting' view with a specific ID returns
    an HTTP 200 response and uses the 'lettings/letting.html' template.
    """

    # Creating a Letting model instance with a specific address
    Letting.objects.create(title="The Burrow", address=address_2)

    # Get URL from view
    url = reverse('lettings:letting', kwargs={"letting_id": 1})
    # Perform a GET request
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/lettings/1/'
    assertTemplateUsed(response, "lettings/letting.html")
