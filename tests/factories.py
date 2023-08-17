import factory
from  factory.django import DjangoModelFactory
from user.models import User, Sms
from salon.models import *


#################### User Factories ######################
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        
    
    full_name = 'ash'
    phone = factory.Sequence(lambda n: f'1234567{n:04d}')
    password = '123'

    
class SmsFactory(DjangoModelFactory):
    class Meta:
        model = Sms
        
    phone = factory.Sequence(lambda n: f'1234567{n:04d}')


#################### Salon Factories #####################
class SalonFactory(DjangoModelFactory):
    class Meta:
        model = Salon
    
    user = factory.SubFactory(UserFactory)
    name = factory.Faker('company')
    phone_number = factory.Sequence(lambda n: f'1234567{n:04d}')


class AmenityFactory(DjangoModelFactory):
    class Meta:
        model = Amenity

    salon = factory.SubFactory(SalonFactory)
    name = factory.Faker('word')


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location
    
    salon = factory.SubFactory(SalonFactory)
    address = 'sample_address'
 
 
class CourtSizeFactory(DjangoModelFactory):
    class Meta:
        model = CourtSize

    
class CourtFactory(DjangoModelFactory):
    class Meta:
        model = Court
    
    salon = factory.SubFactory(SalonFactory)
    name = 'sample_name'
    size = factory.SubFactory(CourtSizeFactory)
    
    
class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review
    
    user = factory.SubFactory(UserFactory)
    name = 'sample_name'
    court = factory.SubFactory(CourtFactory)
    rating = factory.Faker('pyfloat', left_digits=2, right_digits=1, positive=True)
