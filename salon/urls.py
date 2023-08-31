from django.urls import path

from .views.aminity_views import *
from .views.salon_views import *
from .views.location_views import *
from .views.court_views import *
from .views.booking_ref_views import *
from .views.review_views import *
from .views.availableTime_views import *
from .views.reserve_views import *
from .views.wallet_views import *
from .views.site_review_views import *


urlpatterns = [
    
    #salon-image
    path("add_image/", addSalonImage, name="add-Salon-Image"),
    path("delete_image/<str:pk>/", deleteSalonImage, name="delete-Salon-Image"),
    
    
    #Aminity
    path('add_aminity/', addAminity, name='add-amenity'),
    path('get_all_aminity/', getAllAminity, name='get-all-amenity'),
    path('amenity/<str:pk>/', getAminity, name='get-amenity-id'),
    path('update_aminity/<str:pk>/', updateAminity, name='update-amenity-id'),
    path('delete_amenity/<str:pk>/', deleteAminity, name='delete-amenity-id'),
    
    
    #Salon
    path("add_salon/", addSalon, name="add-salon"),
    path("all_salon/", getAllSalon, name="get-all-salon"),
    path("get_salon/<str:pk>/", getSalon, name="get-salon-by-id"),
    path("get_top_rated_salons/", getTopRatedSalons, name="get_top_rated_salons"),
    path("update_salon/<str:pk>/", updateSalon, name="update-salon-by-id"),
    path("delete_salon/<str:pk>/", deleteSalon, name="delete-salon-by-id"),
    
    #Location
    path('location/', location, name='location-list'),
    path('location/<int:pk>/', location, name='location-detail'),
    
    #Court
    path('court/', court, name='court-list'),
    path('court/<int:pk>/', court, name='court-detail'),
    path('court/city/<str:shahrestan>/', courtByShahr, name='get-court-by-city'),
    
    #Booking_Reference
    path('booking_reference/', getBookingReference, name='get-booking-reference'),
    path('booking_reference/<int:pk>/', getBookingReference, name='booking-reference-detail'),
    
    #Review
    path('get_review_by_court_id/<int:court_id>/',getReviewByCourtId , name='get-review-by-court-id'),
    path('add_review/<int:court_id>/',addReview , name='add-review'),
    path('get_review/',getReview , name='get-all-review'),
    path('delete_review/<int:pk>/',getReview , name='delete-review'),

    #Available_Time
    path('available_times/', available_time_list, name='available_time_list'),
    path('available_time_list_by_courtID/<int:court_id>/', available_time_list_by_courtID, name='available_time_list_by_courtID'),
    path('available_time_create/', available_time_create, name='available_time_create'),
    path('available_time_update/<int:pk>/', available_time_update, name='available_time_update'),
    path('available_time_delete/delete/<int:pk>/', available_time_delete, name='available_time_delete'),
    
    
    #Reserve
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/<int:pk>/', reservation_detail, name='reservation_detail'),
    path('reservation_detail_by_userID/', reservation_detail_by_userID, name='reservation_detail_by_userID'),
    path('reservations_create/', reservation_create, name='reservation_create'),
    path('reservations_update/<int:pk>/', reservation_update, name='reservation_update'),
    path('reservations_delete/<int:pk>/', reservation_delete, name='reservation_delete'),
    
    
    #Wallet
    path('get_wallet_balance/', get_wallet_balance, name='get_wallet_balance'),
    path('update_wallet_balance/', update_wallet_balance, name='update_wallet_balance'),
    
    #Site_Review
    path('add_site_review/', addSiteReview, name='post site review'),
]   
