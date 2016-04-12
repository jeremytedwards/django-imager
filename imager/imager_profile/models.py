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
class ImagerAppProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    camera_model = models.CharField(max_length=255)
    nickname = models.CharField(max_length=64)
    friends = models.ManyToManyField(
        'self',
        related_name='friend_of',
        symmetrical=False
    )
    type_of_photography = models.CharField(
        max_length=128,
        choices=PHOTOGRAPHY_TYPES,
    )
    region = models.CharField(
        max_length=3,
        choices=US_REGIONS
    )

    @property
    def is_active(self):
        return self.user.is_active
