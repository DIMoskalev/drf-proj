from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from dogs.models import Breed, Dog
from dogs.serailizers import BreedSerializer, DogSerializer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedCreateAPIView(CreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedListAPIView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedRetrieveAPIView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedUpdateAPIView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDestroyAPIView(DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
