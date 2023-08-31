# import pytest


# pytestmark= pytest.mark.django_db


# class TestSalonModel:
#     def test_salon_str(self, salon_factory):
#         # Arrange
#         # Act
#         x = salon_factory(name='salon_name')
#         # Assert
#         assert x.__str__() == 'salon_name'


# class TestAmenityModel:
#     def test_amenity_str(self, amenity_factory):
#         # Arrange
#         # Act
#         x = amenity_factory(name='sample_amenity')
#         # Assert
#         assert x.__str__() == 'sample_amenity'
        
        
# class TestLocationModel:
#     def test_location_str(self, location_factory):
#         # Arrange
#         # Act
#         x = location_factory(address='sample_address')
#         # Assert
#         assert x.__str__() == 'sample_address'
        
        
# class TestCourtModel:
#     def test_court_str(self, court_factory):
#         # Arrange
#         # Act
#         x = court_factory(name='sample_name')
#         # Assert
#         assert x.__str__() == 'sample_name'


# class TestReviewModel:
#     def test_review_str(self, review_factory):
#         # Arrange
#         # Act
#         x = review_factory(name='sample_name')
#         # Assert
#         assert x.__str__() == 'sample_name'
        
        
# class TestBookingReferenceModel:
#     def test_booking_reference_str(self, booking_reference_factory):
#         # Arrange
#         # Act
#         x = booking_reference_factory(title='sample_title')
#         # Assert
#         assert x.__str__() == 'sample_title'


# class TestTimeSlotModel:
#     def test_time_slot_str(self, time_slot_factory):
#         # Arrange
#         # Act
#         x = time_slot_factory(start_end_time='sample_time')
#         # Assert
#         assert x.__str__() == 'sample_time'



# class TestAvailableTimeModel:
#     def test_available_time_str(self, available_time_factory):
#         # Arrange
#         available_time = available_time_factory()

#         # Act
#         result = str(available_time)

#         # Assert
#         expected_result = f'{available_time.court} {", ".join(map(str, available_time.times.all()))}'
#         assert result == expected_result



# class TestReservationModel:
#     def test_reservation_str(self, reservation_factory):
#         # Arrange
#         reservation = reservation_factory()

#         # Act
#         result = str(reservation)

#         # Assert
#         expected_result = reservation.user.full_name
#         assert result == expected_result



# # class TestWalletModel:
# #     def test_wallet_str(self, wallet_factory, user_factory):
# #         # Arrange
# #         user = user_factory()
# #         wallet = wallet_factory(user=user)

# #         # Act
# #         result = str(wallet)

# #         # Assert
# #         expected_result = user.phone
# #         assert result == expected_result


# class TestSalonImageModel:
#     def test_salon_image_str(self, salon_image_factory):
#         # Arrange
#         salon_image = salon_image_factory(alternative_text='Sample Alternative Text')

#         # Act
#         result = str(salon_image)

#         # Assert
#         expected_result = 'Sample Alternative Text'
#         assert result == expected_result
