import pytest


pytestmark= pytest.mark.django_db



class TestUserModel:
    def test_user_str(self, user_factory):
        # Arrange
        # Act
        x = user_factory()
        # Assert
        assert x.__str__() == 'ash'
    

class TestSmsModel:
    def test_sms_str(self, sms_factory):
        # Arrange
        # Act
        x = sms_factory()
        # Assert
        assert x.__str__() == '12345670000'
            