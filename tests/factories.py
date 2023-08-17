import factory

from user.models import User, Sms


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    
    full_name = 'ash'
    phone = '09186550946'
    password = '123'
    
class SmsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sms
        
    phone = '09186550946'
