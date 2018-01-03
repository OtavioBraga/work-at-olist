from django.core.management.base import BaseCommand, CommandError
from channels.models import Category, Channel
import argparse


class Command(BaseCommand):
    """
        This base command is used to import categories from a file
        to a channel.

        Usage: ./manage.py importcategories <channel> <file.txt>
    """

    help = 'Import categories from a file to a channel'

    def add_arguments(self, parser):
        parser.add_argument('channel', nargs='+', type=str)
        parser.add_argument('file', nargs='+', type=argparse.FileType('r'))

    def file_lines(self, file):
        lines = file.read().split("\n")

        if lines == ['']:
            raise Exception("The file is empty")

        return lines

    def split_categories(self, line):
        return line.split("/")

    def get_categories(self, file):
        categories = [
            self.split_categories(cat)
            for cat in self.file_lines(file)
            if cat != ''
        ]

        return categories

    def get_channel(self, name):
        obj, created = Channel.objects.get_or_create(
            name=name,
        )

        return obj

    def clean_categories(self, channel):
        Category.objects.filter(channel=channel).delete()

    def insert_categories(self, channel, category_line, parent):
        while category_line:
            name = category_line.pop(0).strip()
            parent, created = Category.objects.get_or_create(
                name=name,
                channel=channel,
                parent=parent
            )
            self.insert_categories(channel, category_line, parent)

    def handle(self, *args, **options):
        try:
            file = options.get('file')[0]
            channel_name = options.get('channel')[0]

            category_lines = self.get_categories(file)

            channel = self.get_channel(channel_name)

            self.clean_categories(channel)

            for category_line in category_lines:

                # To avoid category with '' on name we filter
                # te list to remove these empty positions
                filtered_category_line = list(filter(None, category_line))

                self.insert_categories(
                    channel,
                    filtered_category_line,
                    parent=None
                )

            self.stdout.write(self.style.SUCCESS(
                'Successfully imported cats to {}'.format(options['channel']))
            )

        except Exception as e:
            raise e
