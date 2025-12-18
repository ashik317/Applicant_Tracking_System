from django.urls import path

from Authentication.views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path(
        'user/',
        UserListCreateAPIView.as_view(),
        name='Authentication-list-create'
    ),
    path(
        'user/<uuid:alias>/',
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name='Authentication-retrieve-update-destroy'
    ),
]