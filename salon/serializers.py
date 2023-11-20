from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField
from iranian_cities.models import Province, County

class SalonImageSerializer(serializers.ModelSerializer):
    # image = HybridImageField(represent_in_base64=True)
    image = HybridImageField()

    class Meta:
        model = SalonImage
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
        
class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
        
        
class OrderTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTime
        fields = "__all__"


class ReserveSerializer(serializers.ModelSerializer):
    order_time = OrderTimeSerializer(read_only=True)
    
    class Meta:
        model = Reserve
        fields = "__all__"


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = "__all__"
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
        depth=1


class CourtSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField(read_only=True)
    reservations = ReserveSerializer(many=True, read_only=True)
    available_time = AvailableTimeSerializer(many=True, read_only=True)

    class Meta:
        model = Court
        fields = "__all__"
    
    def get_review(self, obj):
        review = obj.review_set.all()
        serializer = ReviewSerializer(review, many=True)
        return serializer.data    
        

class SalonSerializerAll(serializers.ModelSerializer):
    salon_image = SalonImageSerializer(many=True, read_only=True)
    # courts = CourtSerializer(many=True, read_only=True)
    # salon_amenity = AmenitySerializer(many=True, read_only=True)
    # location = LocationSerializer(read_only=True, many=True)
    
    class Meta:
        model = Salon
        fields = "__all__"

class SalonSerializer(serializers.ModelSerializer):
    salon_image = SalonImageSerializer(many=True, read_only=True)
    courts = CourtSerializer(many=True, read_only=True)
    salon_amenity = AmenitySerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True, many=True)
    
    class Meta:
        model = Salon
        fields = "__all__"



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = "__all__"
        
        
        
        
class SiteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteReview
        fields = "__all__"



class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = "__all__"
