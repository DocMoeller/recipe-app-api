from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test user is created with an email succeeded"""
        email = 'nicki.moeller@gmail.com'
        pwd = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=pwd
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(pwd))

    def test_new_user_email_mormalized(self):
        """Test that emails are all lovwrcase"""
        email = 'nicki.moeller@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that an emailadr is provided when creating a new user"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
