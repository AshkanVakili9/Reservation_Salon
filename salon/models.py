from django.db import models
from iranian_cities.fields import ProvinceField, CountyField
from user.models import User
from django.utils.html import mark_safe
from django.conf import settings



class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='ثبت شده در')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name='اپدیت شده در')
    
    class Meta:
        abstract = True

class SalonImage(BaseModel):
    salon = models.ForeignKey(
        "Salon",
        on_delete=models.CASCADE,
        related_name="salon_image", verbose_name='سالن'
    )
    image = models.ImageField(upload_to="salon_image",blank=True, null=True, verbose_name='عکس')
    alternative_text = models.CharField(max_length=100, blank=True, verbose_name='نوشته جایگزین')

    class Meta:
        verbose_name_plural = "عکس سالن ها"    
    
    def __str__(self) -> str:
        return self.alternative_text

    def render_image(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.image))

# امکانات
class Amenity(BaseModel):
    salon = models.ForeignKey('Salon', on_delete=models.CASCADE, related_name='salon_amenity', verbose_name='سالن')
    name = models.CharField(max_length=100, verbose_name='اسم')
    description = models.TextField( verbose_name='توضیحات')
    icon = models.ImageField(upload_to="amenity_icons", verbose_name='ایکون')
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
        "Salon", on_delete=models.PROTECT, blank=True, null=True,related_name='location', verbose_name='سالن'
    )
    ostan = ProvinceField(blank=True, null=True, verbose_name='استان')
    shahrestan = CountyField(blank=True, null=True, verbose_name='شهرستان')
    latitude = models.FloatField(blank=True, null=True, verbose_name='عرض جغرافیایی')
    longitude = models.FloatField(blank=True, null=True, verbose_name='طول جغرافیایی')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='ادرس سالن')

    class Meta:
        verbose_name_plural = "آدرس سالن ها"    
    
    def __str__(self):
        return self.address


class Salon(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='salon')
    name = models.CharField(max_length=100, verbose_name='نام سالن')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    opening_hours = models.CharField(max_length=100, blank=True, null=True, verbose_name='ساعات باز بودن سالن')
    facilities = models.TextField(blank=True, null=True, verbose_name='ساختمان ها')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    contact_email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    website = models.URLField(blank=True, null=True, verbose_name='وبسایت')
    rating = models.FloatField(blank=True, null=True, verbose_name='امتیازات')
    
    class Meta:
        verbose_name_plural = "سالن ها"
        
    def __str__(self):
        return self.name


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='نام')
    court = models.ForeignKey("Court", on_delete=models.CASCADE, verbose_name='نوع زمین ورزشی')
    rating = models.PositiveIntegerField(verbose_name='امتیاز')
    comment = models.TextField(blank=True, null=True, verbose_name='نظر')
    
    class Meta:
        verbose_name_plural = "نظرات"
            
    def __str__(self):
        return f"{self.name}"


class CourtSize(BaseModel):
    SMALL = '5 TO 5'
    MEDIUM = '6 TO 6'
    LARGE = '7 TO 7'
    EXTRA_LARGE = '8 TO 8'
    
    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra_Large'),
    ]

    size = models.CharField(max_length=100, choices=SIZE_CHOICES, default=LARGE, verbose_name='اندازه زمین ورزشی', unique=True)

    class Meta:
        verbose_name_plural = "اندازه زمین"
            
    def __str__(self) -> str:
        return self.size

class Court(BaseModel):
    salon = models.ForeignKey(Salon, on_delete=models.PROTECT, related_name="courts", verbose_name='سالن')
    name = models.CharField(max_length=100, verbose_name='نوع زمین ورزشی(چمن یا سالن فوتسال)')
    size = models.ForeignKey(CourtSize, on_delete=models.PROTECT, verbose_name='اندازه')
    surface_type = models.CharField(max_length=50, verbose_name='جنس کف زمین ')
    amenities = models.ManyToManyField(Amenity, blank=True, verbose_name='امکانات')
    availability = models.BooleanField(blank=True,default=True, null=True, verbose_name='فعال')
    price = models.DecimalField(max_digits=15, decimal_places=0, default=200, verbose_name='قیمت به تومان')
    booking_system = models.CharField(max_length=100, blank=True, null=True, verbose_name='نوع رزرو')
    equipment = models.TextField(blank=True, verbose_name='دستگاه و وسایل ')
    rules = models.TextField(blank=True, verbose_name='قوانین')
    services = models.TextField(blank=True, verbose_name='خدمات')
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='امتیازات')
    numReviews = models.IntegerField(null=True, blank=True, default=0, verbose_name='تعداد نظرات')

    class Meta:
        verbose_name_plural = "نوع سالن ورزشی"
            
    def __str__(self):
        return self.name

class BookingReference(BaseModel):
    title = models.CharField(max_length=200, verbose_name='شماره رزرو')
    
    class Meta:
        verbose_name_plural = "شماره رزرو"
            
    def __str__(self):
        return self.title


class TimeSlot(BaseModel):
    start_end_time = models.CharField(max_length=200, verbose_name='زمان شروع و پایان سانس')

    class Meta:
        verbose_name_plural = "زمان ها"
        
    def __str__(self):
        return f'{self.start_end_time}'



class AvailableTime(BaseModel):
    court = models.ForeignKey("Court", on_delete=models.PROTECT, related_name="available_time", verbose_name='نوع زمین ورزشی')
    times = models.ManyToManyField('TimeSlot', blank=True, verbose_name='زمان')   
    is_booked = models.BooleanField(default=False, verbose_name='رزرو شده')
    
    class Meta:
        verbose_name_plural = "زمان های در دسترس"
        
        
    def __str__(self):
        times_str = ", ".join(str(time) for time in self.times.all())
        return f'{self.court} {times_str}'



class Reservation(BaseModel):
    court = models.ForeignKey("Court", on_delete=models.PROTECT, related_name="reservations", verbose_name='نوع سالن ورزشی')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    available_time = models.ManyToManyField(AvailableTime, blank=True, verbose_name='زمان های در دسترس')
    date = models.DateField(blank=True, null=True, verbose_name='تاریخ')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده')
    additional_notes = models.TextField(blank=True, verbose_name='توضیحات اضافه')
    booking_reference = models.ForeignKey("BookingReference",on_delete=models.CASCADE,blank=True, verbose_name='شماره رزرو')
    is_cancelled = models.BooleanField(default=False, verbose_name='کنسل شده')
    total_amount = models.DecimalField(max_digits=15, decimal_places=0, default=200, verbose_name='کل مبلغ')
    
    class Meta:
        verbose_name_plural = "رزرواسیون"
        
    def __str__(self):
        return self.user.full_name



class Wallet(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet', verbose_name='کاربر')
    balance = models.DecimalField(max_digits=15, decimal_places=0, default=0.00, verbose_name='موجودی')
    
    class Meta:
        verbose_name_plural = "کیف پول"
        
    def __str__(self):
        return f"{self.user.phone}"
