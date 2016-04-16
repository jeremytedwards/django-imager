from django.test import TestCase
from imager_images.models import Photo, Album

import factory

class UserFactory(factory.django.DjangoModelFactory):
    """Define a User factory with a single user."""
    class Meta:
        """Define a model instance class."""
        model = User

    username = 'bob'
    email = 'bob@example.com'


class ImageTestCase(TestCase):
    """Define a class with a series of image tests."""

    def setUp(self):
        """Instance setup factory."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()
        self.album1 = Album(title='album 1', owner=self.user)
        self.album2 = Album(title='album 2', owner=self.user)
        self.image1 = Photo(title='image 1', owner=self.user)
        self.image2 = Photo(title='image 2', owner=self.user)
        self.album1.save()
        self.album2.save()
        self.image1.save()
        self.image2.save()
        self.image1.albums.add(self.album1)

    def test_album(self):
        """Test that profile is created on user save."""
        self.assertTrue(self.user.album)
