from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from salon.serializers import WalletSerializer


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    wallet = WalletSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "phone",
            "password",
            "is_verified",
            "isAdmin",
            "is_active",
            "wallet",
            "updatedAt",
        )
        # fields = '__all__'

    def get_isAdmin(self, obj):
        return obj.is_staff

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "password":
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "phone",
            "isAdmin",
            "is_verified",
            "token",
            "wallet",
        )

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = "__all__"
