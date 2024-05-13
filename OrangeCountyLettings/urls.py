"""
URL configuration for OrangeCountyLettings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    """
    The variable "_" represents division_by_zero
    which is deliberately not used to cause an exception
    and check if sentry is correctly configured.
    """
    _ = 1 / 0


# Configuring custom error handlers
handler404 = 'OrangeCountyLettings.views.custom_404'
handler500 = 'OrangeCountyLettings.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('404/', views.custom_404, name='custom_404'),
    path('500/', views.custom_500, name='custom_500'),
    path('sentry-debug/', trigger_error)
]
