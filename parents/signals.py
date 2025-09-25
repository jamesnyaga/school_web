from django.dispatch import receiver
from. models import Parent, Profile
from django.db.models.signals import post_save

@receiver(post_save, sender=Parent)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(parent=instance)


@receiver(post_save, sender=Parent)
def profile_save(sender,instance, **kwargs):
        instance.profile.save()
