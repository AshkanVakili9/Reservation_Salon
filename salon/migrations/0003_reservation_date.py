# Generated by Django 4.2.4 on 2023-09-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salon", "0002_remove_reservation_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="date",
            field=models.DateField(blank=True, null=True, verbose_name="تاریخ"),
        ),
    ]