# Generated by Django 4.1.7 on 2023-03-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profiles_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profiles",
            name="is_validate",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profiles",
            name="otp",
            field=models.CharField(
                default=1, max_length=6, verbose_name="validation code"
            ),
            preserve_default=False,
        ),
    ]
