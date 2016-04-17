from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
from imager.imager_profile.models import UserProfile

import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class ProfileTestCase2(TestCase):
    """Define a test case to see if testing works."""

    def setUp(self):
        """Set up a user named Robert."""
        self.username = 'Robert'

    def test_robert(self):
        """Assert username created and exits as boo."""
        self.assertEquals(self.username, 'Robert')


class ProfileTestCase(TestCase):
    """Define a class with a series of profile tests."""

    def setUp(self):
        """Instance setup factory."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

    def test_profile(self):
        """Test that profile is created on user save."""
        self.assertTrue(self.user.profile)

    def test_profile_camera_type(self):
        """Test that profile field is created on user save."""
        self.assertEquals(self.user.profile.camera_type, '')

    def test_profile_address(self):
        """Test that profile field is created on user save."""
        self.assertEquals(self.user.profile.address, '')

    def test_profile_web_link(self):
        """Test that profile field is created on user save."""
        self.assertEquals(self.user.profile.web_link, '')

    def test_profile_photo_type(self):
        """Test that profile field is created on user save."""
        self.assertEquals(self.user.profile.photo_type, '')

    def test_profile_social_media(self):
        """Test that profile field is created on user save."""
        self.assertEquals(self.user.profile.social_media, '')

    def test_active(self):
        """Assert that .is_active is True."""
        self.assertTrue(self.user.is_active)

    def test_all_active(self):
        """Assert that the user profile is in the list or active profiles."""
        self.assertIn(self.user.profile, UserProfile.active.all())

    def test_all_active_len(self):
        """All active's have a length of one."""
        self.assertEquals(len(UserProfile.active.all()), 1)

    def test_deactivate(self):
        """Assert that .is_active can be set to false correctly."""
        self.user.is_active = False
        self.assertFalse(self.user.is_active)

    def test_deactivate_later(self):
        """Test that non active users is not in all actives."""
        self.user.is_active = False
        self.user.save()
        self.assertNotIn(self.user.profile, UserProfile.active.all())


class Cleanup_Users(ProfileTestCase):
    """Define a class that deletes bob."""

    def setUp(self):
        """Set up a factory of a deleted bob."""
        super(Cleanup_Users, self).setUp()
        self.user.delete()

    def test_all_active(self):
        """Test to see if bob is not in the active lists."""
        self.assertNotIn(self.user.profile, UserProfile.active.all())

    def test_all_active2(self):
        """Assert that there are no entries that are active."""
        self.assertEquals(len(UserProfile.active.all()), 0)
