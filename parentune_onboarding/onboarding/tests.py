import uuid
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Parent, Child, Blog


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent = Parent.objects.create(
            name="Dhruv", email="dhruvyadav@gmail.com", parent_type="first_time"
        )
        self.child = Child.objects.create(
            age_group="infant", gender="male", parent=self.parent
        )
        self.blog = Blog.objects.create(
            title="Test Blog",
            content="Test Content",
            age_group="infant",
            gender="male",
            parent_type="first_time",
            link=f"https://example.com/{uuid.uuid4()}",
            snippet="Test Snippet",
            preview_image="https://example.com/test-blog.jpg",
            description="Test Description",
        )

    def test_generate_home_feed(self):
        response = self.client.get(
            "/api/update-home-feed/",
            {
                "age_group": "infant",
                "gender": "male",
                "parent_type": "first_time",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_home_feed_view(self):
        response = self.client.get(
            "/api/home-feed/",
            {
                "age_group": "infant",
                "gender": "male",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
