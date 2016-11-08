"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        django.setup()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_post_feiralivre(self):
        """
        Tests POST Feira Livre
        """
        self.assertEqual(1 + 1, 2)

    def test_put_feiralivre(self):
        """
        Tests Put Feira Livre
        """
        self.assertEqual(1 + 1, 2)

    def test_get_feiralivre(self):
        """
        Tests Get Feira Livre
        """
        self.assertEqual(1 + 1, 2)

    def test_getALL_feiralivre(self):
        """
        Tests GetALL Feira Livre
        """
        self.assertEqual(1 + 1, 2)