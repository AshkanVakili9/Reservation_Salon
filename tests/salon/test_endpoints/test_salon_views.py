import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import json

pytestmark = pytest.mark.django_db



# @pytest.mark.xfail
# class TestSalonEndpoints:
#     endpoint = '/salon/all_salon/'
    
#     def test_get_all_salon(self, salon_factory, api_client):
#         salon_factory.create_batch(5)
#         response = api_client.get(self.endpoint)
#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 5
