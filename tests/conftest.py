from pytest_factoryboy import register
from .factories import *
import pytest
from rest_framework.test import APIClient



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
register(BookingReferenceFactory)
register(TimeSlotFactory)
register(AvailableTimeFactory)
register(ReservationFactory)
# register(WalletFactory)
register(SalonImageFactory)



@pytest.fixture
def api_client():
    return APIClient()
