from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from polls import apiviews


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
        request.user = self.user
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            f'Expected Response Code 200, '
            f'received {response.status_code} instead.'
        )

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {"question": "How are you?", "created_by": 1}
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code, 404,
            f'Expected Response Code 404, '
            f'received {response.status_code} instead.'
        )
