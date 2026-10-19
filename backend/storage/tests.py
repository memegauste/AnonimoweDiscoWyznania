"""Check the backend against the supported Python and Django versions."""

# Standard Library
import importlib
from unittest.mock import patch

# Django
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Local
from .models import Designate


class BackendCompatibilityTests(TestCase):
    """Exercise HTTP responses, model storage and admin rendering."""

    def test_index_reports_online(self):
        """Return the backend health response as JSON."""
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'online': True})

    def test_designation_defaults(self):
        """Persist a new designation awaiting approval."""
        designation = Designate.objects.create(message='Przykładowe wyznanie')
        designation.refresh_from_db()

        self.assertEqual(designation.message, 'Przykładowe wyznanie')
        self.assertFalse(designation.approved)
        self.assertIsNotNone(designation.created_dt)

    def test_admin_lists_designations(self):
        """Render stored designations in the admin change list."""
        user = get_user_model().objects.create_user(
            username='admin', is_staff=True, is_superuser=True,
        )
        self.client.force_login(user)
        Designate.objects.create(message='Wyznanie do moderacji')

        response = self.client.get(reverse('admin:storage_designate_changelist'))

        self.assertContains(response, 'Wyznanie do moderacji')

    def test_discord_bot_initializes(self):
        """Initialize the bot and register its anonymous submission command."""
        with patch('utils.read_json_file', return_value={'token': 'unused'}):
            bot = importlib.import_module('main')

        self.assertTrue(bot.client.intents.message_content)
        self.assertIsNotNone(bot.tree.get_command('anonim'))
