from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from polls import apiviews
from django.test import TestCase


class TestPoll(APITestCase):
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test', email='testuser@test.com', password='test'
        )

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            f'Expected Response Code 200, '
            f'received {response.status_code} instead.'
        )
