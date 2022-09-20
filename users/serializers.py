from django.contrib.auth import authenticate, get_user_model
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from ecommerce.models import Customer


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for object user
    """

    class Meta:
        model = get_user_model()
        fields = ("__all__")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5,
            }
        }

    def create(self, **validated_data):
        """
        Create new user with encrypted password and return it
        """

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates user and return correct configurated password
        """

        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

            return user


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["__all__"]
