# Generated by Django 4.2.4 on 2023-08-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Amenity",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                ("name", models.CharField(max_length=100, verbose_name="اسم")),
                ("description", models.TextField(verbose_name="توضیحات")),
                (
                    "icon",
                    models.ImageField(upload_to="amenity_icons", verbose_name="ایکون"),
                ),
                ("active", models.BooleanField(default=True, verbose_name="فعال")),
            ],
            options={
                "verbose_name_plural": "امکانات",
            },
        ),
        migrations.CreateModel(
            name="AvailableTime",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "is_booked",
                    models.BooleanField(default=False, verbose_name="رزرو شده"),
                ),
            ],
            options={
                "verbose_name_plural": "زمان های در دسترس",
            },
        ),
        migrations.CreateModel(
            name="BookingReference",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                ("title", models.CharField(max_length=200, verbose_name="شماره رزرو")),
            ],
            options={
                "verbose_name_plural": "شماره رزرو",
            },
        ),
        migrations.CreateModel(
            name="Court",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        verbose_name="نوع زمین ورزشی(چمن یا سالن فوتسال)",
                    ),
                ),
                (
                    "surface_type",
                    models.CharField(max_length=50, verbose_name="جنس کف زمین "),
                ),
                (
                    "availability",
                    models.BooleanField(
                        blank=True, default=True, null=True, verbose_name="فعال"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=0,
                        default=200,
                        max_digits=15,
                        verbose_name="قیمت به تومان",
                    ),
                ),
                (
                    "booking_system",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="نوع رزرو"
                    ),
                ),
                (
                    "equipment",
                    models.TextField(blank=True, verbose_name="دستگاه و وسایل "),
                ),
                ("rules", models.TextField(blank=True, verbose_name="قوانین")),
                ("services", models.TextField(blank=True, verbose_name="خدمات")),
                (
                    "rating",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=7,
                        null=True,
                        verbose_name="امتیازات",
                    ),
                ),
                (
                    "numReviews",
                    models.IntegerField(
                        blank=True, default=0, null=True, verbose_name="تعداد نظرات"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "نوع سالن ورزشی",
            },
        ),
        migrations.CreateModel(
            name="CourtSize",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("5 TO 5", "Small"),
                            ("6 TO 6", "Medium"),
                            ("7 TO 7", "Large"),
                            ("8 TO 8", "Extra_Large"),
                        ],
                        default="7 TO 7",
                        max_length=100,
                        unique=True,
                        verbose_name="اندازه زمین ورزشی",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "اندازه زمین",
            },
        ),
        migrations.CreateModel(
            name="Location",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "latitude",
                    models.FloatField(
                        blank=True, null=True, verbose_name="عرض جغرافیایی"
                    ),
                ),
                (
                    "longitude",
                    models.FloatField(
                        blank=True, null=True, verbose_name="طول جغرافیایی"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="ادرس سالن"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "آدرس سالن ها",
            },
        ),
        migrations.CreateModel(
            name="Reservation",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                ("date", models.DateField(blank=True, null=True, verbose_name="تاریخ")),
                (
                    "is_paid",
                    models.BooleanField(default=False, verbose_name="پرداخت شده"),
                ),
                (
                    "additional_notes",
                    models.TextField(blank=True, verbose_name="توضیحات اضافه"),
                ),
                (
                    "is_cancelled",
                    models.BooleanField(default=False, verbose_name="کنسل شده"),
                ),
                (
                    "total_amount",
                    models.DecimalField(
                        decimal_places=0,
                        default=200,
                        max_digits=15,
                        verbose_name="کل مبلغ",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "رزرواسیون",
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="نام"
                    ),
                ),
                ("rating", models.PositiveIntegerField(verbose_name="امتیاز")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="نظر"),
                ),
            ],
            options={
                "verbose_name_plural": "نظرات",
            },
        ),
        migrations.CreateModel(
            name="Salon",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                ("name", models.CharField(max_length=100, verbose_name="نام سالن")),
                (
                    "phone_number",
                    models.CharField(
                        max_length=11, unique=True, verbose_name="شماره تلفن"
                    ),
                ),
                (
                    "opening_hours",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="ساعات باز بودن سالن",
                    ),
                ),
                (
                    "facilities",
                    models.TextField(blank=True, null=True, verbose_name="ساختمان ها"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="توضیحات"),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="ایمیل"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="وبسایت"),
                ),
                (
                    "rating",
                    models.FloatField(blank=True, null=True, verbose_name="امتیازات"),
                ),
            ],
            options={
                "verbose_name_plural": "سالن ها",
            },
        ),
        migrations.CreateModel(
            name="SalonImage",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="salon_image",
                        verbose_name="عکس",
                    ),
                ),
                (
                    "alternative_text",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="نوشته جایگزین"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "عکس سالن ها",
            },
        ),
        migrations.CreateModel(
            name="TimeSlot",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "start_end_time",
                    models.CharField(
                        max_length=200, verbose_name="زمان شروع و پایان سانس"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "زمان ها",
            },
        ),
        migrations.CreateModel(
            name="Wallet",
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
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="ثبت شده در"),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, verbose_name="اپدیت شده در"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=0,
                        default=0.0,
                        max_digits=15,
                        verbose_name="موجودی",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "کیف پول",
            },
        ),
    ]