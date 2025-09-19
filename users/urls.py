from django.urls import path

from users.views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path(
        'user/',
        UserListCreateAPIView.as_view(),
        name='users-list-create'
    ),
    path(
        'user/<uuid:alias>/',
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name='users-retrieve-update-destroy'
    ),
]