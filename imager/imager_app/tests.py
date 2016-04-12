from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User

import factory
from imager.imager_app.models import ImagerAppProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@dobalina.com',
        )
        self.user.set_password('secret')

    def test_user_has_profile(self):
        self.assertTrue(self.user.profile)