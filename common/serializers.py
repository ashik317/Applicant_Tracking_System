from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CommonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "title",
            "first_name",
            "middle_name",
            "last_name",
        ]

