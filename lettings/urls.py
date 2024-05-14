"""
URL configuration module for the 'lettings' application.

This module contains the configuration of URLs for the 'lettings' application.
It defines the paths of URLs associated with the 'index' and 'letting' views
in the 'views' module.
"""

from django.urls import path
from . import views

#  Declares the namespace (app_name) for lettings application URLs
app_name = "lettings"

# Defining application URL patterns
urlpatterns = [
    path("", views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting')
]
