
from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='user-update')

]
