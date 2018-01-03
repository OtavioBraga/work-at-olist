from django.urls import reverse
from rest_framework.test import APITestCase
from channels.models import Category, Channel
from channels.serializers import ChannelSerializer
from django.core.management import call_command, CommandError
from django.test import TestCase
from django.utils.six import StringIO
import os


class ImportCommandTestCase(TestCase):

    def setUp(self):
        tests_path = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.join(tests_path, 'test_files/categories.txt')
        self.channel = 'test_channel'
        self.category = 'Desktop'
        self.command = 'importcategories'
        self.assert_message = 'Successfully imported categories to {}\n'.format(
            self.channel
        )

        # Defined out to avoid printing the command message on tests
        out = StringIO()
        call_command(self.command, self.channel, self.file, stdout=out)

    def test_if_arguments_is_required(self):
        with self.assertRaises(CommandError):
            call_command(self.command)

    def test_command_output(self):
        out = StringIO()
        call_command(
            self.command,
            self.channel,
            self.file,
            stdout=out,
            no_color=True
        )
        self.assertEquals(out.getvalue(), self.assert_message)

    def test_if_channel_is_created(self):
        self.assertTrue(Channel.objects.get(name=self.channel))

    def test_if_last_category_is_created(self):
        self.assertTrue(Category.objects.get(name=self.category))

    def test_number_of_categories_created(self):
        self.assertEqual(Category.objects.count(), 23)


class ChannelAPIViewTestCase(APITestCase):
    """
        Tests for the Channel list and detail views
    """

    def setUp(self):
        self.list_channels_url = reverse("channels:channels-list")
        self.channel = Channel.objects.create(name='Test Channel')

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

    def test_channel_detail_page_for_200(self):
        """
            Test to verify if chanel detail page returns 200
        """

        response = self.client.get(self.channel_detail_url)
        self.assertEqual(200, response.status_code)

    def test_invalid_channel_detail_page(self):
        """
            Test to verify if a invalid channel uuid returns 404
        """

        response = self.client.get(self.invalid_channel_detail_url)
        self.assertEqual(404, response.status_code)


class CategoryAPIViewTestCase(APITestCase):
    """
        Tests for Category list and detail pages
    """

    def setUp(self):
        self.list_categories_url = reverse("channels:categories-list")

        self.channel = Channel.objects.create(name='Test Channel 2')

        self.parent_category = Category.objects.create(
            name='Test Category',
            channel=self.channel
        )
        self.parent_category_url = reverse(
            "channels:category-detail",
            kwargs={"uuid": self.parent_category.uuid}
        )

        self.child_category = Category.objects.create(
            name='Test Category',
            parent=self.parent_category,
            channel=self.channel
        )
        self.child_category_url = reverse(
            "channels:category-detail",
            kwargs={"uuid": self.child_category.uuid}
        )

        self.category_detail_url = reverse(
            "channels:category-detail",
            kwargs={"uuid": self.child_category.uuid}
        )

        self.invalid_category_detail_url = reverse(
            "channels:category-detail",
            kwargs={"uuid": "ff45bb27-68c9-42de-9fbe-e00a9ea7ea87"}
        )

    def test_category_list_page_for_200(self):
        """
            Test to verify if the list of categories returns 200
        """

        response = self.client.get(self.list_categories_url)
        self.assertEqual(200, response.status_code)

    def test_category_detail_page_for_200(self):
        """
            Test to verify if a parent or child category detail page
            returns 200.
        """

        response = self.client.get(self.parent_category_url)
        self.assertEqual(200, response.status_code)

        response = self.client.get(self.child_category_url)
        self.assertEqual(200, response.status_code)

    def test_invalid_category_detail_page(self):
        """
            Test to verify if a invalid category uuid returns 404
        """

        response = self.client.get(self.invalid_category_detail_url)
        self.assertEqual(404, response.status_code)
