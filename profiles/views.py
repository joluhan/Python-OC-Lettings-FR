"""
View definition module for the 'profiles' application.

This module defines views for the 'profiles' application, which are responsible
for managing HTTP requests and return appropriate responses.
Views include an index view showing the list of profiles and
an individual profile view showing details of a specific profile.

Functions:
     index: View to display the list of profiles.
     profile: View to display details of a specific profile.
"""

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Profile


def index(request):
    """
    View to display the list of profiles.

    Args:
    request (HttpRequest): Object representing the HTTP request.

    Returns:
    HttpResponse: HTTP response containing the list of profiles
    rendered in a template.
    """
    profiles_list = get_list_or_404(Profile)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View to display details of a specific profile.

    Args:
    request (HttpRequest): Object representing the HTTP request.
    username (str): Profile username.

    Returns:
    HttpResponse: HTTP response containing profile details
    rendered in a template.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
