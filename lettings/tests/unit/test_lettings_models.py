"""
Unit testing module for the 'lettings' application models.

This module contains unit tests for the Address and
Letting from the 'lettings' application.
Tests verify instance creation, representation
as a string, and other features application templates.
"""

import pytest
from django.test import Client
from lettings.models import Letting, Address


client = Client()


@pytest.mark.django_db
def test_address_model():
    """
    Unit test for the Address model of the 'lettings' application.

    This test creates an instance of the Address model, verifies
    that its representation as a string is correct and matches
    the expected value.
    """
    address = Address.objects.create(
        number=4,
        street="Privet Drive",
        city="Little Whinging",
        state="EA",
        zip_code=47839,
        country_iso_code="UK",
    )
    expected_value = "4 Privet Drive"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model():
    """
    Unit test for the Letting model of the 'lettings' application.

    This test creates an instance of the Letting model, verifies
    that its representation as a string is correct and matches the
    expected value.
    """
    address = Address.objects.create(
        number=4,
        street="Privet Drive",
        city="Little Whinging",
        state="EA",
        zip_code=47839,
        country_iso_code="UK",
    )
    letting = Letting.objects.create(title="Harry Potter's House",
                                     address=address)
    expected_value = "Harry Potter's House"
    assert str(letting) == expected_value
