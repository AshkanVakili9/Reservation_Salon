# Generated by Django 4.2.4 on 2023-08-17 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sms",
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
                ("phone", models.CharField(max_length=11, verbose_name="شماره تلفن")),
                ("sms", models.CharField(max_length=6, verbose_name="اس ام اس")),
                (
                    "is_matched",
                    models.BooleanField(default=False, verbose_name="تایید شده"),
                ),
                (
                    "sentDate",
                    models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال"),
                ),
            ],
            options={
                "verbose_name_plural": "اس ام اس",
            },
        ),
        migrations.CreateModel(
            name="User",
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
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="نام و نام خانوادگی",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=11, unique=True, verbose_name="شماره تلفن"
                    ),
                ),
                ("password", models.CharField(max_length=200, verbose_name="رمز عبور")),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="کاربر ادمین"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="فعال")),
                (
                    "is_verified",
                    models.BooleanField(default=False, verbose_name="تایید احراز هویت"),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="زمان ثبت نام"
                    ),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "کاربر ها",
            },
        ),
    ]