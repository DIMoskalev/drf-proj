from django.urls import path
from rest_framework.routers import SimpleRouter

from dogs.apps import DogsConfig
from dogs.views import (
    BreedCreateAPIView,
    BreedDestroyAPIView,
    BreedListAPIView,
    BreedRetrieveAPIView,
    BreedUpdateAPIView,
    DogViewSet,
)

app_name = DogsConfig.name

router = SimpleRouter()
router.register("", DogViewSet)

urlpatterns = [
    path("breeds/", BreedListAPIView.as_view(), name="breeds-list"),
    path("breeds/<int:pk>/", BreedRetrieveAPIView.as_view(), name="breed-retrieve"),
    path("breeds/<int:pk>/update/", BreedUpdateAPIView.as_view(), name="breed-update"),
    path("breeds/<int:pk>/delete/", BreedDestroyAPIView.as_view(), name="breed-delete"),
    path("breeds/create/", BreedCreateAPIView.as_view(), name="breed-create"),
] + router.urls
