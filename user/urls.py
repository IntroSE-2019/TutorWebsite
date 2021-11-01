from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:UUID>', views.user, name='user'),
]