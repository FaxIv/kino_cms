"""kinocms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from .views import *

urlpatterns = [
    path('', base),
    path('banners/', banners),
    path('movies/', movies),
    path('cinemas/', cinemas),
    path('news/', news),
    path('promotions/', promotions),
    path('pages/', pages),
    path('mailing/', mailing),
    path('movies/moviepage/', movie_create),
    path('movies/<int:pk>/update/', movie_update, name='movie-update'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie-delete'),

]
