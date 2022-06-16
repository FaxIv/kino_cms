
from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('logout_cms/', LogoutStaffUser.as_view(), name='logout_cms'),
    path('<int:pk>/update/', user_edit, name='user-update'),
    path('mailing/', mailing_view, name='mailing'),
    path('mailing/select-user/', MailingUsersView.as_view(), name='select-user'),

]
