from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='stephen.cftai@gmail.com',
            password='P@ssw0rd1'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='tai101448339@gmail.com',
            password='P@ssw0rd1',
            name='Test User Fullname',)

    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
