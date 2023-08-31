# Generated by Django 4.2.4 on 2023-08-31 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("salon", "0003_alter_amenity_updatedat_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitereview",
            name="User",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
    ]