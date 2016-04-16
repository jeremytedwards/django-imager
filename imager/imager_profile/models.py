# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class ActiveProfileManager(models.Manager):
    """convenience manager which returns only active profiles"""
    def get_queryset(self):
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('sports', 'Sports'),
]
US_REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('ne', 'New England'),
    ('ma', 'Mid-Atlantic'),
    ('se', 'Southeast'),
    ('mw', 'Midwest'),
    ('ds', 'Deep South'),
    ('sw', 'Southwest'),
    ('cf', 'California'),
    ('ak', 'Alaska'),
    ('hi', 'Hawaii')
]


@python_2_unicode_compatible
class UserProfile(models.Model):
    """Create a unique profile for a user."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        primary_key=True,
    )
    camera_type = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=60, blank=True)
    web_link = models.CharField(max_length=70, blank=True)
    photo_type = models.CharField(max_length=30, blank=True)
    social_media = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, choices=US_REGIONS,
                              default='North America')

    friends = models.ManyToManyField("self", symmetrical=False,
                                     related_name='friend_of')
    objects = models.Manager()
    active = ActiveProfileManager()

    @property
    def is_active(self):
        """Property to define if user is active."""
        return self.user.is_active

    def __str__(self):
        """Hand back username's profile."""
        return "{}'s profile".format(self.user.username)
