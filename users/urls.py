from django.urls import path
from .views import (
    home,
    register_owner,
    register_borrower
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'register-owner/',
        register_owner,
        name='register_owner'
    ),

    path(
        'register-borrower/',
        register_borrower,
        name='register_borrower'
    ),
]