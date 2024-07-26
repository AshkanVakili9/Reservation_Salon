# Generated by Django 4.2.4 on 2023-09-12 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("salon", "0004_remove_availabletime_court_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="availabletime",
            old_name="times",
            new_name="time",
        ),
        migrations.AlterField(
            model_name="ordertime",
            name="reserve",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="order_time",
                to="salon.reserve",
            ),
        ),
    ]