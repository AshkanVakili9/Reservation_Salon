import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

pytestmark = pytest.mark.django_db




@pytest.mark.xfail
def test_list_salons(api_client):
    url = reverse('salon-list')  # Adjust this to your URL name
    
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
