from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class Sms(models.Model):
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    sms = models.CharField(max_length=6, verbose_name='اس ام اس')
    is_matched = models.BooleanField(default=False, verbose_name='تایید شده')
    sentDate = models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')

    class Meta:
        verbose_name_plural = "اس ام اس"

    def __str__(self):
        return f"{self.phone}"


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=11, unique=True, blank=False, null=False, verbose_name='شماره تلفن')
    password = models.CharField(max_length=200, verbose_name='رمز عبور')

    is_staff = models.BooleanField(default=False, verbose_name='کاربر ادمین')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_verified = models.BooleanField(default=False, verbose_name='تایید احراز هویت')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='زمان ثبت نام')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name='اپدیت شده در')
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = "کاربر ها"

    def __str__(self):
        return f"{self.full_name}"
