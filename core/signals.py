from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache


@receiver(post_save)
def post_model_save(sender, instance, **kwargs):
    """
    Clear cache when any kind of Model is saved
    """
    cache.clear()
