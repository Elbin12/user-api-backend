from django.test import TestCase

from users.models import CustomUser

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

# Create your tests here.

class UserViewTests(APITestCase):

    def setUp(self):
        """Create some test users for our tests."""
        self.user1 = CustomUser.objects.create(
            first_name="James", last_name="Smith", company_name= 'Tech Corp', age=30, city="New York", state="NY", zip="10001", email="james@example.com", web="http://james.com"
        )
        self.user2 = CustomUser.objects.create(
            first_name="John", last_name="Doe", age=25, company_name= 'Tech Corp', city="Los Angeles", state="CA", zip="90001", email="john@example.com", web="http://john.com"
        )
        self.client = APIClient()  # Create a test client for making API calls

    def test_get_users_with_name_filter(self):
        """Test the name query parameter."""
        response = self.client.get('/api/users/', {'name': 'James'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return only one user

    def test_get_users_with_sorting(self):
        """Test sorting users by age."""
        response = self.client.get('/api/users/', {'sort': '-age'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['first_name'], 'James')  # James should come first since he is older

    def test_get_users_with_pagination(self):
        """Test pagination functionality."""
        response = self.client.get('/api/users/', {'page': 1, 'limit': 1})  # Only 1 user per page
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return only one user on the first page

    def test_post_create_user(self):
        """Test the POST method to create a new user."""
        data = {
            'first_name': 'Alice',
            'last_name': 'Wonderland',
            'company_name': 'Tech Corp',
            'age': 28,
            'city': 'Wonderland',
            'state': 'WA',
            'zip': '20001',
            'email': 'alice@example.com',
            'web': 'http://alice.com'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 3)  # There should be 3 users now
