import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from booking.models import FitnessClass, Booking

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def fitness_class():
    return baker.make(FitnessClass, total_slots=10, available_slots=10)


def test_list_classes(api_client, fitness_class):
    resp = api_client.get(reverse("class-list"))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()[0]["name"] == fitness_class.name


def test_successful_booking(api_client, fitness_class):
    from django.contrib.auth.models import User

    user = User.objects.create_user("ayushsenapati", "ayushsenapati@omnify.com", "ayushsenapati_omnify")
    token = api_client.post(reverse("token_obtain_pair"),{"username": user.username, "password": "ayushsenapati_omnify"},format="json",).json()["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    resp = api_client.post(
        reverse("book"),
        {
            "fitness_class": fitness_class.id,
            "client_name": "Test",
            "client_email": "t@e.com",
        },
        format="json",
    )

    assert resp.status_code == status.HTTP_201_CREATED
    fitness_class.refresh_from_db()
    assert fitness_class.available_slots == 9


def test_overbooking(api_client, fitness_class):
    fitness_class.available_slots = 0
    fitness_class.save()

    from django.contrib.auth.models import User

    user = User.objects.create_user("ayushsenapati02", "ayushsenapati02@omnify.com", "ayushsenapati02_omnify")
    token = api_client.post(reverse("token_obtain_pair"),{"username": user.username, "password": "ayushsenapati02_omnify"},format="json",).json()["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    resp = api_client.post(
        reverse("book"),
        {
            "fitness_class": fitness_class.id,
            "client_name": "Test",
            "client_email": "t@e2.com",
        },
        format="json",
    )
    assert resp.status_code == status.HTTP_400_BAD_REQUEST


def test_list_bookings_by_email(api_client, fitness_class):
    baker.make(Booking, fitness_class=fitness_class, client_email="a@b.com")
    baker.make(Booking, fitness_class=fitness_class, client_email="c@d.com")

    from django.contrib.auth.models import User

    user = User.objects.create_user("ayushsenapati03", "ayushsenapati03@omnify.com", "ayushsenapati03_omnify")
    token = api_client.post(reverse("token_obtain_pair"),{"username": user.username, "password": "ayushsenapati03_omnify"},format="json",).json()["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    resp = api_client.get(f"{reverse('booking-list')}?client_email=a@b.com")
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 1
    assert resp.json()[0]["client_email"] == "a@b.com"
