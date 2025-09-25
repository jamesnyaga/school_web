from django.dispatch import receiver
from. models import Teacher, profile
from django.db.models.signals import post_save

@receiver(post_save, sender=Teacher)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(teacher=instance)


@receiver(post_save, sender=Teacher)
def profile_save(instance, sender, **kwargs):
        instance.profile.save()
