from unittest.mock import patch
import pytest
from django.urls import reverse
from rest_framework import status
from user.models import Sms


pytestmark = pytest.mark.django_db


class TestUserRegisterEndPoints:
    endpoint = '/user/register/'
    user_data = {
            'full_name': 'test_name',
            'phone': '09186550946',
            'password': '123',
            'confirm_password': '123'
        }
    
    @patch('user.views.sms_send')
    def test_successful_user_registration(self, send_sms_mock, api_client):
        response = api_client.post(self.endpoint, data=self.user_data)
        assert response.status_code == 201
        assert send_sms_mock.call_count == 1
    
    @patch('user.views.sms_send')
    def test_password_matching(self, api_client, send_sms_mock):
        response = api_client.post(self.endpoint, data=self.user_data)
        assert response.status_code == 400
        assert send_sms_mock.call_count == 0
    
    
    # @patch('user.views.sms_send')
    # def test_verify_code(self, send_sms_mock, user_factory, api_client): 
    #     endpoint = '/user/verifycode/'
    #     data = {'code': '123456'}
    #     user = user_factory.create()
    #     # Authenticate the API client with the user
    #     api_client.force_authenticate(user=user)

    #     # Make a POST request to the endpoint
    #     response = api_client.post(endpoint, data=data)

    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.data["message"] == "sms is true"

    #     # Reload the user instance from the database to get the updated data
    #     user.refresh_from_db()
    #     assert user.is_verified is True
    #     assert sms.is_matched is True
            
            
        
        
    
    # @patch('user.views.sms_send')
    # def test_send_sms_endpoint(self, send_sms_mock, user_factory, api_client):
    #     endpoint = '/user/sendSms/'
    #     # Create a user instance using the user_factory
    #     user = user_factory.create()
        
    #     # Mock the sms_send function to return True
    #     send_sms_mock.return_value = True
    #     # Prepare the data for your request
    #     data = {
    #         'phone': user.phone,
    #         'code': '245789'  
    #     }
        
        
    #     api_client.force_authenticate(user=user)
        
    #     # Make a POST request to the endpoint
    #     response = api_client.post(endpoint, data, format='json')
        
    #     # Assertions
    #     assert response.status_code == status.HTTP_200_OK
    #     assert send_sms_mock.call_count == 1  # Check that sms_send was called once    
