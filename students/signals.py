from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile, Student

@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(student=instance)


@receiver(post_save, sender=Student)
def profile_save(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Student)
def update_user_email(sender, instance, **kwargs):
    if instance.user.email != instance.email:
        instance.user.email = instance.email
        instance.user.save(update_fields=['email'])