# Generated by Django 4.2.7 on 2024-09-04 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0015_infra_end_latitude_infra_end_longitude"),
    ]

    operations = [
        migrations.CreateModel(
            name="BridgePicture",
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
                ("image", models.ImageField(upload_to="photos/")),
                ("picture_number", models.IntegerField()),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="infra.article"
                    ),
                ),
                (
                    "infra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.infra",
                        verbose_name="橋梁名",
                    ),
                ),
            ],
        ),
    ]
