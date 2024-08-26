from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        help_text="Укажите номер телефона",
        **NULLABLE
    )
    tg_nick = models.CharField(
        max_length=50,
        verbose_name="Tg name",
        help_text="Укажите ник в телеграмм",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Donation(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name="Сумма пожертвования",
        help_text="Укажите сумму пожертвования",
    )
    sessions_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        help_text="Укажите ID сессии",
        **NULLABLE,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на пожертвование",
        help_text="Укажите ссылку на пожертвование",
        **NULLABLE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"

    def __str__(self):
        return f"Пожертвование на сумму {self.amount} рублей"
