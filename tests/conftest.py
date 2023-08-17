from pytest_factoryboy import register
from .factories import *

#################### User Factories ######################
register(UserFactory)
register(SmsFactory)


#################### Salon Factories #####################
register(SalonFactory)
register(AmenityFactory)
register(LocationFactory)
register(CourtSizeFactory)
register(CourtFactory)
register(ReviewFactory)
