"""
Unit testing module for 'lettings' application views.

This module contains unit tests for views
'index' and 'letting' of the 'lettings' application.
The tests verify that the views return
HTTP 200 responses with appropriate templates and content
of the pages corresponds to the expected information.
"""

import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_lettings_index_view(address_1, address_2):
    """
    Unit test for the 'index' view of the 'lettings' application.

    This test creates instances of Letting models, verifies that the
    'lettings_index' view returns an HTTP 200 response with the template
    'lettings/index.html' and the content of the page includes
    the expected information.
    """
    # Creating Letting template instances with specific addresses
    Letting.objects.create(title="Harry Potter's House", address=address_1)
    Letting.objects.create(title="The Burrow", address=address_2)

    # Using reverse() to get URL of view 'index'
    path = reverse("lettings:lettings_index")

    # Sending an HTTP GET request to the URL obtained with reverse()
    response = client.get(path)
    content = response.content.decode()

    # Checking the contents of the index page
    expected_content = '<a href="/lettings/1/">Harry Potter&#x27;s House</a>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings_letting_view(address_2):
    """
    Unit test for the 'letting' view of the 'lettings' application.

    This test creates a Letting model instance, verifies that the
    'letting' view with a specific ID returns an HTTP 200 response
    with the template 'lettings/letting.html' and the content of
    the page includes the expected information.
    """
    # Creating a Letting model instance with a specific address
    Letting.objects.create(title="The Burrow", address=address_2)

    # Using reverse() to get URL of 'letting' view with specific ID
    path = reverse("lettings:letting", kwargs={'letting_id': 1})

    # Sending an HTTP GET request to the URL obtained with reverse()
    response = client.get(path)
    content = response.content.decode()

    # Checking the content of the details page for Letting
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">The Burrow</h1>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
