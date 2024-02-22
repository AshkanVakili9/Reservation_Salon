import factory
from faker import Faker
from  factory.django import DjangoModelFactory
from user.models import User, Sms
from salon.models import *

fake = Faker()

#################### User Factories ######################
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        
    
    full_name = factory.Faker("name")
    phone = factory.Sequence(lambda n: f'1234567{n:04d}')
    password = factory.Faker("password")
    
    
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
    phone_number = factory.Sequence(lambda n: f'0912345678{n:02d}')


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
 

    
class CourtFactory(DjangoModelFactory):
    class Meta:
        model = Court
    
    salon = factory.SubFactory(SalonFactory)
    name = 'sample_name'

    
    
class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review
    
    user = factory.SubFactory(UserFactory)
    name = 'sample_name'
    court = factory.SubFactory(CourtFactory)
    rating = factory.Faker('pyfloat', left_digits=2, right_digits=1, positive=True)



class TimeSlotFactory(DjangoModelFactory):
    class Meta:
        model = TimeSlot
    
    start_end_time = factory.Faker('sentence', nb_words=4)
        
class AvailableTimeFactory(DjangoModelFactory):
    class Meta:
        model = AvailableTime

    court = factory.SubFactory(CourtFactory)  
    is_booked = factory.Faker('boolean')

    @factory.post_generation
    def times(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for time in extracted:
                self.times.add(time)


class ReservationFactory(DjangoModelFactory):
    class Meta:
        model = Reserve

    court = factory.SubFactory(CourtFactory)  # Replace with appropriate factory
    user = factory.SubFactory(UserFactory)
    is_paid = factory.Faker('boolean')
    additional_notes = factory.Faker('text')




# class WalletFactory(DjangoModelFactory):
#     class Meta:
#         model = Wallet

#     user = factory.SubFactory(UserFactory)
#     balance = factory.Faker('pydecimal', right_digits=0, min_value=0, max_value=999999999999999)  # Adjust the range as needed



class SalonImageFactory(DjangoModelFactory):
    class Meta:
        model = SalonImage

    salon = factory.SubFactory(SalonFactory)
    image = factory.django.ImageField()
    alternative_text = factory.Faker('sentence', nb_words=6)
