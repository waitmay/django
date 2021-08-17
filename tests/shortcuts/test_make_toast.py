from django.test import SimpleTestCase
from django.shortcuts import make_toast


class MakeToastTest(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(make_toast(), 'toast')
