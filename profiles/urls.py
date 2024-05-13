"""
Module for defining URLs for views of the 'profiles' application.

This module defines the URLs for the views of the 'profiles' application.
It associates the views to the corresponding URL paths, using the URL names
to reference the views.

Variables:
    app_name (str): Application name used to create URL namespaces.
    urlpatterns (list): List of URL patterns associating views
    with corresponding paths.
"""

from django.urls import path
from . import views

# Application name used to create URL namespaces.
app_name = "profiles"

# List of URL patterns associating views with corresponding paths.
urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
