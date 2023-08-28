from unittest.mock import patch
import pytest
from django.urls import reverse
from rest_framework import status
# from user.views import sms_send

pytestmark = pytest.mark.django_db


class TestUserEndpoints:
    user_data = {
            'full_name': 'test_name',
            'phone': '09186550946',
            'password': '123',
            'confirm_password': '123'
        }
    
    @patch('user.views.sms_send')
    def test_register_new_user(self, send_sms_mock, api_client):
        endpoint = '/user/register/'
        response = api_client.post(endpoint, data=self.user_data)
        assert response.status_code == 201
        assert send_sms_mock.call_count == 1


    @patch('user.views.sms_send')
    def test_send_sms_endpoint(self, send_sms_mock, user_factory, api_client):
        endpoint = '/user/sendSms/'
        # Create a user instance using the user_factory
        user = user_factory.create()
        
        # Mock the sms_send function to return True
        send_sms_mock.return_value = True
        # Prepare the data for your request
        data = {
            'phone': user.phone,
            'code': '245789'  # Replace with the actual template ID
        }
        
        api_client.force_authenticate(user=user)
        # Make a POST request to the endpoint
        response = api_client.post(endpoint, data, format='json')
        
        # Assertions
        assert response.status_code == status.HTTP_200_OK
        assert send_sms_mock.call_count == 1  # Check that sms_send was called once    
