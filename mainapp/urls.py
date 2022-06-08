from django.urls import path
from .views import *
from users.views import LoginUser, LogoutUser, RegisterUser

urlpatterns = [
    path('', main_page, name='main_page'),
    # path('', index, name='main_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),

]
