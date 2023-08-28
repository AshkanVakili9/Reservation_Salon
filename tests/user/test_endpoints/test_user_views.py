# from unittest.mock import patch
# import pytest
# from user.models import User
# from user.serializers import UserSerializer
# pytestmark = pytest.mark.django_db


# class TestUserRegister:
#     endpoint = '/user/register/'
#     @pytest.fixture
#     def user_data(self):
#         return {
#             "full_name": "John Doe",
#             "phone": "09186550946",
#             "password": "test123",
#             "confirm_password": "test123",
#         }

#     def test_successful_user_registration(self, api_client, user_data):
#         response = api_client.post(self.endpoint, user_data, format="json")
#         assert response.status_code == 201
#         assert "id" in response.data

#         user = User.objects.get(phone=user_data["phone"])
#         assert user.full_name == user_data["full_name"]
#         assert user.phone == user_data["phone"]

#         serializer = UserSerializer(user)
#         assert response.data == serializer.data

#     def test_missing_required_fields(self, api_client):
#         response = api_client.post(self.endpoint, {}, format="json")
#         assert response.status_code == 400
#         assert "error" in response.data

#     def test_passwords_mismatch(self, api_client, user_data):
#         user_data["confirm_password"] = "mismatched_password"
#         response = api_client.post(self.endpoint, user_data, format="json")
#         assert response.status_code == 400
#         assert "error" in response.data

#     @pytest.fixture
#     def existing_user(self,user_factory):
#         return user_factory(phone="09182470021")

#     def test_existing_user(self, api_client, existing_user, user_data):
#         user_data["phone"] = existing_user.phone
#         response = api_client.post(self.endpoint, user_data, format="json")
#         assert response.status_code == 400
#         assert "error" in response.data
