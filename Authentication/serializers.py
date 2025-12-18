from rest_framework import serializers

from common.serializers import CommonUserSerializer
from Authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    alias = serializers.UUIDField(read_only=True)
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    created_by = CommonUserSerializer(read_only=True)
    updated_by = CommonUserSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'alias',
            'email',
            'password',
            'phone',
            'title',
            'first_name',
            'middle_name',
            'last_name',
            'profile_image',
            'nid',
            'user_type',
            'city',
            'state',
            'country',
            'zip_code',
            'address',
            'created_by',
            'updated_by',
            'updated_at',
            'created_at',
        ]
        read_only_fields = [
            'alias',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        req = self.context.get('request')
        if req:
            if req.method in("PUT", "PATCH"):
                self.fields.pop('email', None)
                self.fields.pop('password', None)

            elif req.method == "POST":
                self.fields["password"].required = True

    def create(self, validated_data):
        request = self.context.get("request")
        password = validated_data.pop("password")

        validated_data.pop("created_by", None)
        validated_data.pop("updated_by", None)

        user = User(**validated_data)
        user.set_password(password)

        if getattr(request, "user", None) and request.user.is_authenticated:
            user.created_by = request.user

        user.updated_by = None

        user.save()
        return user

    def update(self, instance, validated_data):
        request = self.context.get("request")
        password = validated_data.pop("password", None)

        validated_data.pop("email", None)
        #validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if getattr(instance, "updated_by_id", None) is None:
            data["updated_by"] = None
        return data