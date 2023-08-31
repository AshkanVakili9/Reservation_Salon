from django.contrib import admin
from .models import *

# Register your models here.

class SalonImageAdmin(admin.ModelAdmin):
    # readonly_fields=('',)
    list_display = ['pk','alternative_text', 'render_image']
    search_fields = ['alternative_text']
    list_filter = ['alternative_text']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['salon','ostan', 'shahrestan', 'address']
    search_fields = ['salon', 'ostan', 'shahrestan']
    list_filter = ['salon', 'ostan']

class SalonAdmin(admin.ModelAdmin):
    list_display = ['user', 'name','phone_number', 'rating']
    search_fields = ['phone_number',]
    
    
class CourtAdmin(admin.ModelAdmin):
    list_display = ['name','salon', 'availability', 'size', 'price', 'rating']
    search_fields = ['name', 'salon']
    list_filter = ['availability']
    
    
class CourtSizeAdmin(admin.ModelAdmin):
    list_display = ['size']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'court', 'booking_reference', 'is_paid', 'is_cancelled','total_amount']
    search_fields = ['user', 'additional_notes', 'court']

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields=('rating', 'comment')
    list_display = ['name', 'user', 'rating', 'court']
    search_fields =['name', 'user']
    
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name', 'salon', 'active', 'render_image']
    search_fields =['name', 'salon']


class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ['court', 'is_booked']
    search_fields =['court', 'salon']    

    
    
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields =['user']    

class SiteReviewAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields =['user'] 
    
admin.site.register(SalonImage, SalonImageAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(CourtSize, CourtSizeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(AvailableTime, AvailableTimeAdmin)
admin.site.register(Wallet, WalletAdmin)

admin.site.register(BookingReference)
admin.site.register(TimeSlot)
admin.site.register(SiteReview, SiteReviewAdmin)
