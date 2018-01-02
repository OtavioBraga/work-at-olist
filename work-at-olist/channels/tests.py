import json
from django.urls import reverse

from rest_framework.test import APITestCase
from channels.models import Category, Channel
from channels.serializers import ChannelSerializer


class ChannelAPIViewTestCase(APITestCase):

    def setUp(self):
        self.list_channels_url = reverse("channels:channels-list")
        self.channel = Channel.objects.create(name='Canal teste')

        self.channel_detail_url = reverse(
            "channels:channel-detail",
            kwargs={"uuid": self.channel.uuid}
        )

        self.invalid_channel_detail_url = reverse(
            "channels:channel-detail",
            kwargs={"uuid": "ff45bb27-68c9-42de-9fbe-e00a9ea7ea87"}
        )

    def test_channels_list_page_for_200(self):
        """
        Test to verify if the list of channels returns 200
        """

        response = self.client.get(self.list_channels_url)
        self.assertEqual(200, response.status_code)

    def test_channel_detail_page(self):
        """
        Test to verify if chanel detail page returns 200
        """

        response = self.client.get(self.channel_detail_url)
        self.assertEqual(200, response.status_code)

    def test_invalid_channel_detail_page(self):
        """
            Test to verify if a invalid channel uuid return 404
        """

        response = self.client.get(self.invalid_channel_detail_url)
        self.assertEqual(404, response.status_code)
