import pytest


pytestmark= pytest.mark.django_db


class TestSalonModel:
    def test_salon_str(self, salon_factory):
        # Arrange
        # Act
        x = salon_factory(name='salon_name')
        # Assert
        assert x.__str__() == 'salon_name'


class TestAmenityModel:
    def test_amenity_str(self, amenity_factory):
        # Arrange
        # Act
        x = amenity_factory(name='sample_amenity')
        # Assert
        assert x.__str__() == 'sample_amenity'
        
        
class TestLocationModel:
    def test_location_str(self, location_factory):
        # Arrange
        # Act
        x = location_factory(address='sample_address')
        # Assert
        assert x.__str__() == 'sample_address'
        
        
class TestCourtModel:
    def test_court_str(self, court_factory):
        # Arrange
        # Act
        x = court_factory(name='sample_name')
        # Assert
        assert x.__str__() == 'sample_name'


class TestReviewModel:
    def test_review_str(self, review_factory):
        # Arrange
        # Act
        x = review_factory(name='sample_name')
        # Assert
        assert x.__str__() == 'sample_name'
