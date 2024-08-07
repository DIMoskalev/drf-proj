from rest_framework.serializers import ModelSerializer

from dogs.models import Breed, Dog


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
