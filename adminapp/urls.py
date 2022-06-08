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
from users.views import LoginUser


urlpatterns = [
    path('', base, name='welcome_page'),

    path('statistic/', statistic),

    path('banners/', banners, name='banners'),

    path('movies/', movies),
    path('movies/moviepage/', movie_create),
    path('movies/<int:pk>/update/', movie_update, name='movie-update'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie-delete'),

    path('cinemas/', cinemas),
    path('cinemas/cinema_page/', cinema_create, name='cinema-create'),
    path('cinemas/<int:pk>/cinema_update/', cinema_update, name='cinema-update'),
    path('cinemas/<int:pk>/cinema_delete/', cinema_delete, name='cinema-delete'),
    path('cinemas/<int:cinema_pk>/hall_create/', hall_create, name='hall-create'),
    path('cinemas/<int:cinema_pk>/hall_update/<int:pk>/', hall_update, name='hall-update'),
    path('cinemas/<int:cinema_pk>/hall_delete/<int:pk>/', hall_delete, name='hall-delete'),

    path('news/', news),
    path('promotions/', promotions),
    path('<str:article_type>/create/', article_create, name='article-create'),
    path('<str:article_type>/<int:pk>/update/', article_update, name='article-update'),
    path('<str:article_type>/<int:pk>/delete/', article_delete, name='article-delete'),

    path('pages/', pages_base),
    path('pages/pages_base/', pages_create, name='pages-create'),
    path('pages/<int:pk>/pages_update/', pages_update, name='pages-update'),
    path('pages/<int:pk>/pages_base_delete/', pages_delete, name='pages-delete'),
    path('pages/main_page/', main_page_update, name='main-page-update'),
    path('pages/cinema_contacts/', cinema_contacts_update, name='cinema-contacts-update'),
]
