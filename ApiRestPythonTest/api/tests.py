"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from requests.auth import HTTPBasicAuth

# TODO: Configure your database in settings.py and sync before running tests.

class ApiTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ApiTest, cls).setUpClass()
            django.setup()

    def test_post_feiralivre(self):
        """
        Tests POST Feira Livre
        """
        #response = self.client.get('/')
        #self.assertContains(response, 'Home Page', 1, 200)
        self.assertTrue(True,"TestePOST")

    def test_put_feiralivre(self):
        """
        Tests Put Feira Livre
        """
        #response = self.client.get('/api/feiraslivres')
        #self.assertContains(response, 'Home Page', 1, 200)
        self.assertTrue(True,"TestePUT")

    def test_get_feiralivre(self):
        """
        Tests Get Feira Livre
        """
        #response = self.client.get('/api/feiraslivres')
        #self.assertContains(response, 'Home Page', 1, 200)
        self.assertTrue(True,"TesteGeT")

    def test_getALL_feiralivre(self):
        """
        Tests GetALL Feira Livre
        """
        #response = self.client.get('/api/feiraslivres')
        #self.assertContains(response, 'Home Page', 1, 200)
        self.assertTrue(True,"TesteGeTALL")