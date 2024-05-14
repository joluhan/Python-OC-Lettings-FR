"""
This module defines several views, including the main view ('index') and
custom views for handling 404 and 500 errors. These views use specific
templates to render associated pages.
"""

from django.shortcuts import render
from sentry_sdk import capture_message


# View for the 'index' home page.
def index(request):
    # This view renders the home page using the 'index.html' template.
    return render(request, 'index.html')


# View for handling 404 errors.
def custom_404(request, *args, **kwargs):
    """
    This view renders the 404 error page using the '404.html' template and
    returns a response with HTTP status 404.
    """
    # Log in case of 404 error
    capture_message("page not found !", level='error')
    return render(request, "404.html", status=404)


# View for handling 500 errors.
def custom_500(request, *args, **kwargs):
    """
    This view renders the 500 error page using the '500.html' template and
    returns a response with HTTP status 500.
    """
    # Log in case of 500 error
    capture_message("Server Error !", level='error')
    return render(request, "500.html", status=500)
