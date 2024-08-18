from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Breed(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Порода", help_text="Укажите породу"
    )
    description = models.TextField(
        verbose_name="Описание породы", help_text="Добавьте описание", **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
        help_text="Укажите владельца"
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Укажите кличку"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода",
        help_text="Выберите породу",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
        **NULLABLE
    )
    date_born = models.DateTimeField(
        verbose_name="Дата рождения", help_text="Укажите дату рождения", **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
        help_text="Укажите владельца собаки"
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
