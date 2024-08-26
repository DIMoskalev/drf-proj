from rest_framework.serializers import ModelSerializer

from users.models import User, Donation


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone",)


class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = ("id", "amount", "sessions_id", "link", "user",)
