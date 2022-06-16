from django.urls import path
from .views import *
from users.views import LoginUser, LogoutUser, RegisterUser

app_name = 'mainapp'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),

    path('poster/', PosterView.as_view(), name='poster'),
    path('soon/', SoonView.as_view(), name='soon'),

    path('cinemas/', CinemasView.as_view(), name='cinemas'),

    path('promotions/', article_view, name='promotions'),
    path('promotions/<int:pk>', ContactsView.as_view(), name='promotion-note'),
    path('news/', article_view, name='news'),
    path('news/<int:pk>', ContactsView.as_view(), name='news-note'),

    path('contacts/', ContactsView.as_view(), name='contacts'),


    path('pages/<str:type>/', BasePageView.as_view(), name='base_site_page')

]
