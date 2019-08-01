# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import GuardianRestAPI
from .serializers import GuardianRestAPISerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_news(sectionName="", webTitle=""):
        if sectionName != "" and webTitle != "":
            GuardianRestAPI.objects.create(sectionName=sectionName, webTitle=webTitle)

    def setUp(self):
        # add test data
        self.create_news("like glue", "sean paul")
        self.create_news("simple song", "konshens")
        self.create_news("love is wicked", "brick and lace")
        self.create_news("jam rock", "damien marley")


class GetAllNewsTest(BaseViewTest):

    def test_get_all_news(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("news-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = GuardianRestAPI.objects.all()
        serialized = GuardianRestAPISerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)