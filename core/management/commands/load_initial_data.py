import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        fixtures_dir = os.path.join(settings.PROJECT_ROOT, settings.SITE_NAME, 'core', 'fixtures')
        fixture_file = os.path.join(fixtures_dir, 'initial_data.json')

        call_command('loaddata', fixture_file, verbosity=3)
