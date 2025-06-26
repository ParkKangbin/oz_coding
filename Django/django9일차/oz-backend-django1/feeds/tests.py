from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class FeedAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "testuser", password = 'password')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer{self.token}')


        self.feed1 = Feed.objects.create(user=self.user,title = 'Title 1')
        self.feed2 = Feed.objects.create(user=self.user,title = 'Title 2')
    
    def test_get_all(self):
        url = reverse('all_feeds')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data),2)

    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs = {'feed_id':1})
        res = self.client.get(url)

        self.assertEqual(res.status_code,status.HTTP_200_OK)
        # self.assertEqual(len(res.data),2)
        self.assertEqual(res.data['title'],self.feed1.title)

    def test_create_feed(self):
        url = reverse('all_feeds')  # 이게 POST를 받는 view에 연결돼 있어야 해요

        data = {'content': 'New Feed Content', 'title': 'New Title'}

        # ✅ 강제 인증 방식으로 처리
        self.client.force_authenticate(user=self.user)

        res = self.client.post(url, data)

        # 결과 확인
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Feed.objects.count(), 3)  # 기존 2개 + 1개 = 3개
        self.assertEqual(Feed.objects.latest('id').content, 'New Feed Content')