from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    This template represents an address with fields such as number,
    the street, city, state, zip code and country ISO code.
    The __str__ method is defined to provide a string representation
    of the object.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)]
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model representing a rental (letting).

     This template represents a rental with a title and address
     associated (OneToOne relationship with Address).
     The __str__ method is defined to provide a
     string representation of the object.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
