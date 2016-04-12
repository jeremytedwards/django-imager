# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from imager_profile.models import ImagerAppProfile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ensure_imager_profile(sender, instance=None, created=None, **kwargs):
    if created:
        try:
            new_profile = ImagerAppProfile(user=instance)
            new_profile.save()
        except ValueError:
            logger.error("Unable to create ImagerProfile for {}".format(instance))

@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_imager_profile(sender, instance=None, **kwargs):
    try:
        instance.profile.delete()
    except AttributeError:
        logger.warn(
            "ImagerProfile instance is not deleted for {}; perhaps it does not exist?"
                .format(instance)
        )