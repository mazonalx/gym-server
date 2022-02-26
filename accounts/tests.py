from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',username='normaluser',
            first_name='Normal', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.username, 'normaluser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(str(user), 'normal@user.com')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='',username = '',password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='super@user.com',username='superuser'
            ,password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.username, 'superuser')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(str(admin_user), 'super@user.com')
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com',username='superuser',
                password='foo', is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com',username='superuser',
                password='foo', is_staff=False)