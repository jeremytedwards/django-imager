# coding=utf-8
from django.conf import settings
from django.db import models


class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


def user_file_store_path(instance, filename):
    """File will be uploaded to MEDIA_ROOT/user_{id}/{filename}"""
    return "user_{0}/{1}".format(instance.user.id, filename)


class ImagerAppProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    # cameratype, photography, location, friends
    friends = models.ManyToManyField('self', related_name='friend_of', symmetrical=False)
    # inspector thinks Manager needs a 'what' parameter
    # noinspection PyArgumentList
    objects = models.Manager()
    active = ActiveProfileManager()

    @property
    def is_active(self):
        return self.user.is_active


class PostedImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_images')
    file = models.ImageField(upload_to=user_file_store_path)


class ImageAlbum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='image_albums')
    images = models.ManyToManyField(PostedImage, related_name='albums')