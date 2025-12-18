from django.shortcuts import render
from rest_framework.generics import (
ListCreateAPIView,
RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from Authentication.models import User
from Authentication.serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return(
            User.objects
            .select_related(
                "created_by",
                "updated_by",
            )
        )

    def perform_create(self, serializer):
        serializer.save()

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'alias'

    def get_queryset(self):
        return (
            User.objects
            .select_related(
                "created_by",
                "updated_by",
            )
        )

    def perform_update(self, serializer):
        user=self.request.user
        if user.is_authenticated:
            serializer.save(updated_by=self.request.user)
        else:
            raise ValueError("User must be authenticated to update this field.")

    def perform_destroy(self, instance):
        instance.delete()
