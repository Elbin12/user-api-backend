
from django.urls import path

from .views import UserDetailView, UsersListCreateView

urlpatterns = [
    path('users/', UsersListCreateView.as_view()),
    path('users/<int:id>/', UserDetailView.as_view())
]