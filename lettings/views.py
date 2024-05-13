from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Letting


def index(request):
    """
    View to display the list of rentals.

    This view retrieves the list of rentals using the get_list_or_404 function
    and returns a response rendered from the 'lettings/index.html' template.
    """
    lettings_list = get_list_or_404(Letting)
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View to display details for a specific rental.

    This view retrieves details of a specific rental using the function
    get_object_or_404 and returns a response rendered from the
    'lettings/letting.html' template.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
