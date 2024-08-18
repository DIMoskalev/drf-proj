# Generated by Django 5.1 on 2024-08-18 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="breed",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="dog",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца собаки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
