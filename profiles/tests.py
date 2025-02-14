from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='asd', password='svQeniPl')

    def test_can_list_posts(self):
        asd = User.objects.get(username='asd')
        Post.objects.create(owner=asd, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
