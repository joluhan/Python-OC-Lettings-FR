Database Structure and Models
============================================================

“lettings” application
----------------------------
The "lettings" application defines two main models in the database.

1 Address: This template represents an address with the following fields:

- number: Street number (positive integer).
- street: Name of the street.
- city: Name of the city.
- state: State (two-character ISO code).
- zip_code: Postal code (positive integer).
- country_iso_code: ISO code of the country (three characters).

2 Letting: This template represents a rental with the following fields:

- title: Title of the rental.
- address: OneToOne relationship with the Address model, representing the address associated with the location.

Profiles app
----------------------------

The "profiles" application defines a template in its database.

Profile: This template represents a user profile with the following fields:
user: OneToOne relationship with the Django user model (User).
favorite_city: User's favorite city (character string, optional).

The User Class
-------------

The User class is provided by Django and manages user authentication information,
such as username, password, etc.

UML diagram
-----------

.. image::_static/oc_lettings_uml.png
    :alt: uml schema of the database
