import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db



def test_api_schema_generated_successfully(admin_client):
    url = reverse("api-schema")
    response = admin_client.get(url)
    assert response.status_code == 200
