# Generated by Django 4.1.7 on 2023-02-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="model_cards",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="model_cars"
                    ),
                ),
                (
                    "data",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="data_time_models_cars"
                    ),
                ),
            ],
            options={
                "ordering": ("data",),
            },
        ),
    ]