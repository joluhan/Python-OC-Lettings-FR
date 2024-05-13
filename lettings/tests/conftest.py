"""
Configuration module for testing the 'lettings' application.

This module contains fixtures that are used in tests
unitary and integration to provide data
pre-configured (like Address and Letting template instances)
to simplify the creation and execution of tests.
"""

import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address_1():
    """
    Fixture to create an Address model instance with specific values.

    This fixture creates and returns an instance
    of the Address model with predefined values.
    It is used in tests to provide a specific address.
    """
    address = Address.objects.create(
        number=4,
        street="Privet Drive",
        city="Little Whinging",
        state="EA",
        zip_code=47839,
        country_iso_code="UK",
    )
    return address


@pytest.fixture
def address_2():
    """
    Fixture to create a second Address model instance
    with specific values.

    This fixture creates and returns a second instance
    of the Address model with predefined values.
    It is used in testing to provide a second specific address.
    """
    address = Address.objects.create(
        number=12,
        street="Square Grimmaurd",
        city="Loutry Ste Chaspoule",
        state="DE",
        zip_code=89654,
        country_iso_code="UK",
    )
    return address


@pytest.fixture
def letting_1(address_1):
    """
    Fixture to create a Letting model instance linked to address_1.

    This fixture creates and returns an instance of the Letting model
    with predefined values and linked to the address provided as a parameter.
    It is used in testing to provide a specific Letting linked to
    a specific address.
    """
    letting = Letting.objects.create(title="Harry Potter's House", address=address_1)
    return letting


@pytest.fixture
def letting_2(address_2):
    """
    Fixture to create a second instance of
    Letting model linked to address_2.

    This fixture creates and returns a second instance
    of the Letting model with predefined values
    and linked to the address provided as a parameter. She is
    used in testing to provide a second specific Letting linked to
    a second specific address.
    """
    letting = Letting.objects.create(title="The Burrow", address=address_2)
    return letting
