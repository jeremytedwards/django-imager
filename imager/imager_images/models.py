# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.db import models


def user_file_store_path(instance, filename):
    """File will be uploaded to MEDIA_ROOT/user_{id}/{filename}"""
    return "user_{0}/{1}".format(instance.user.id, filename)

# [('value', 'visible')]
PUB_CHOICES = [(-1, 'Private'), (0, 'Shared'), (1, 'Public')]

class PostedImage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posted_images'
    )
    file = models.ImageField(
        upload_to=user_file_store_path
    )
    # title = models.
    # description = models.
    # date_uploaded = models.DateField(auto_now_add=True)
    # date_modified = models.DateField(auto_now=True)
    # date_published = models.DateField() # set in the UI
    published = models.CharField(
        max_length=3,
        choices=PUB_CHOICES,
        default=-1
    )


    def __str__(self):
        # TODO: build the object here?
        return self.title

# Users should be able to designate one contained photo as the ‘cover’ for the album.
# The albums created by a user may contain only Photos created by that same user.
class ImageAlbum(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='image_albums'
    )
    images = models.ManyToManyField(
        PostedImage,
        related_name='albums'
    )
    # cover = models.ManyToManyField(
    #     PostedImage,
    #     related_name='cover'
    # )
    # title = models.
    # description = models.
    # date_uploaded = models.DateField(auto_now_add=True)
    # date_modified = models.DateField(auto_now=True)
    # date_published = models.DateField()
    # published = (‘private’, ‘shared’, ‘public’)

    def __str__(self):
        return self.title


