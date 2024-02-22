import datetime
import os
from django.db import models
from iranian_cities.fields import ProvinceField, CountyField
from django.utils.html import mark_safe
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
   createdAt = models.DateTimeField(
      auto_now_add=True, editable=False, verbose_name='ثبت شده در')
   updatedAt = models.DateTimeField(
      auto_now=True, verbose_name='آپدیت شده در')

   class Meta:
      abstract = True


""" Save static files in folders based on the current time  """

def date_helper():
    now = datetime.date.today()
    formatted_date = now.strftime("%Y-%m-%d")  
    return formatted_date

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def salon_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    today_date = date_helper()
    folder_path = f"salon_image/{today_date}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return os.path.join(folder_path, final_name)

""" End  """



class SalonImage(BaseModel):
   salon = models.ForeignKey(
      "Salon",
      on_delete=models.CASCADE,
      related_name="salon_image", verbose_name='سالن'
   )
   image = models.ImageField(upload_to=salon_image_path,
                           blank=True, null=True, verbose_name='عکس')
   alternative_text = models.CharField(
      max_length=100, blank=True, verbose_name='نوشته جایگزین')

   class Meta:
      verbose_name_plural = "عکس سالن ها"

   def __str__(self) -> str:
      return self.alternative_text

   def render_image(self):
      if self.image != '':
         return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.image))

# امکانات
class Amenity(BaseModel):
   salon = models.ForeignKey('Salon', on_delete=models.CASCADE,
                           related_name='salon_amenity', verbose_name='سالن')
   name = models.CharField(max_length=100, verbose_name='اسم')
   description = models.TextField(verbose_name='توضیحات', blank=True)
   icon = models.ImageField(upload_to="amenity_icons", verbose_name='ایکون', blank=True)
   active = models.BooleanField(default=True, verbose_name='فعال')

   class Meta:
      verbose_name_plural = "امکانات"

   def __str__(self):
      return self.name

   def render_image(self):
      if self.icon != '':
         return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.icon))


class Location(BaseModel):
   salon = models.ForeignKey(
      "Salon", on_delete=models.CASCADE, related_name='location', verbose_name='سالن'
   )
   ostan = ProvinceField(blank=True, verbose_name='استان')
   shahrestan = CountyField(blank=True, verbose_name='شهرستان')
   latitude = models.FloatField(
      blank=True, null=True, verbose_name='عرض جغرافیایی')
   longitude = models.FloatField(
      blank=True, null=True, verbose_name='طول جغرافیایی')
   address = models.CharField(
      max_length=200, blank=True, verbose_name='ادرس سالن')

   class Meta:
      verbose_name_plural = "آدرس سالن ها"

   def __str__(self):
      return self.address


class Salon(BaseModel):
   user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='salon')
   name = models.CharField(max_length=100, verbose_name='نام سالن')
   phone_number = models.CharField(
      max_length=11, unique=True, verbose_name='شماره تلفن')
   opening_hours = models.CharField(
      max_length=100, blank=True, null=True, verbose_name='ساعات باز بودن سالن')
   facilities = models.TextField(
      blank=True, null=True, verbose_name='ساختمان ها')
   description = models.TextField(
      blank=True, null=True, verbose_name='توضیحات')
   contact_email = models.EmailField(
      blank=True, null=True, verbose_name='ایمیل')
   rating = models.FloatField(blank=True, null=True, verbose_name='امتیازات')

   class Meta:
      verbose_name_plural = "سالن ها"

   def __str__(self):
      return self.name


class Court(BaseModel):
   salon = models.ForeignKey(
      Salon, on_delete=models.CASCADE, related_name="courts", verbose_name='سالن')
   name = models.CharField(
      max_length=100, verbose_name='نوع زمین ورزشی(چمن یا سالن فوتسال)')
   surface_type = models.CharField(max_length=50, verbose_name='جنس کف زمین ')
   amenities = models.ManyToManyField(
      Amenity, blank=True, verbose_name='امکانات')
   availability = models.BooleanField(
      blank=True, default=True, null=True, verbose_name='فعال')
   price = models.DecimalField(
      max_digits=15, decimal_places=0, default=200, verbose_name='قیمت به تومان')
   booking_system = models.CharField(
      max_length=100, blank=True, null=True, verbose_name='نوع رزرو')
   equipment = models.TextField(blank=True, verbose_name='دستگاه و وسایل ')
   rules = models.TextField(blank=True, verbose_name='قوانین')
   services = models.TextField(blank=True, verbose_name='خدمات')
   rating = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='امتیازات')
   numReviews = models.IntegerField(
      null=True, blank=True, default=0, verbose_name='تعداد نظرات')

   class Meta:
      verbose_name_plural = "نوع سالن ورزشی"

   def __str__(self):
      return f'{self.name}'

class Ball(BaseModel):
   price = models.DecimalField(max_digits=15, decimal_places=0, default=20000, verbose_name='مبلغ اجاره توپ')

   class Meta:
      verbose_name_plural = "اجاره توپ"

   def __str__(self):
      return f'{self.price}'
   

class Review(BaseModel):
   user = models.ForeignKey(
      User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
   name = models.CharField(max_length=200, null=True,
                           blank=True, verbose_name='نام')
   court = models.ForeignKey(
      "Court", on_delete=models.CASCADE, verbose_name='نوع زمین ورزشی')
   rating = models.PositiveIntegerField(verbose_name='امتیاز')
   comment = models.TextField(blank=True, null=True, verbose_name='نظر')

   class Meta:
      verbose_name_plural = "نظرات"

   def __str__(self):
      return f"{self.name}"


   
class TimeSlot(BaseModel):
   start_end_time = models.CharField(max_length=200,
                                     verbose_name='زمان شروع و پایان سانس')

   class Meta:
      verbose_name_plural = "زمان ها"

   def __str__(self):
      return f'{self.start_end_time}'


class AvailableTime(BaseModel):
   court = models.ForeignKey("Court", on_delete=models.CASCADE, verbose_name='نوع زمین ورزشی', null=True, blank=True)
   time = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, verbose_name='زمان', null=True, blank=True)
   date = models.DateField(blank=True, null=True, verbose_name='تاریخ رزرو')
   is_booked = models.BooleanField(default=False, verbose_name='رزرو شده')
   discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='تخفیف')
   
   class Meta:
      verbose_name_plural = "زمان های در دسترس"

   def __str__(self):
      return f'{self.court} ---- {self.date}'
 
 
# order
class Reserve(BaseModel):
   user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
   payment_method = models.CharField(max_length=200, verbose_name='نوع پرداخت', null=True, blank=True, default='اینترنتی')
   total_amount = models.DecimalField(max_digits=15, decimal_places=0, default=200, verbose_name='کل مبلغ')
   paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
   is_paid = models.BooleanField(default=False)
   payment_number = models.CharField(max_length=200, verbose_name='شماره رزرو', blank=True)

   class Meta:
      verbose_name_plural = "رزرو"

   def __str__(self):
      return f"{self.user.full_name}"


# order item
class OrderTime(BaseModel):
   available_time = models.ManyToManyField('AvailableTime', blank=True,  null=True, related_name='تایم های رزروی')
   reserve = models.ForeignKey('Reserve', on_delete=models.SET_NULL, null=True, related_name='سبد خرید')
   price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='مبلغ')
   
   class Meta:
      verbose_name_plural = "تایم های رزروی"
   
   def __str__(self) -> str:
      return str(self.available_time)


class Wallet(BaseModel):
   user = models.OneToOneField(User, 
      on_delete=models.CASCADE, related_name='wallet', verbose_name='کاربر')
   balance = models.DecimalField(
      max_digits=15, decimal_places=0, default=0.00, verbose_name='موجودی')

   class Meta:
      verbose_name_plural = "کیف پول"

   def __str__(self):
      return f"{self.user.phone}"


class SiteReview(BaseModel):
   user = models.ForeignKey(
      User, on_delete=models.CASCADE, verbose_name='کاربر', blank=True)
   text = models.TextField(verbose_name='نظر')

   class Meta:
      verbose_name_plural = "نظرات در مورد سایت"

   def __str__(self):
      return f"{self.user.full_name}"



class Discount(models.Model):
   percent = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='درصد تخفیف')

   class Meta:
      verbose_name_plural = "تخفیف‌ها"

   def __str__(self):
      return f'{self.percent} درصد تخفیف'
