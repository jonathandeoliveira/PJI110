# Generated by Django 5.0.3 on 2024-05-13 23:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_userprofile_full_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="document",
            field=models.CharField(
                max_length=14,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="O CPF deve ter 11 dígitos, exemplo: 19876543210.",
                        regex="^\\d{11}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="full_address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Insira o telefone com o DDD, exemplo: 11912341234.",
                        regex="^\\d{11}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="postal_code",
            field=models.CharField(
                max_length=12,
                validators=[
                    django.core.validators.RegexValidator(
                        message="O CEP deve ter 8 dígitos, exemplo: 12345678.",
                        regex="^\\d{8}$",
                    )
                ],
            ),
        ),
    ]
