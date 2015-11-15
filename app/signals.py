from django.db.models import Count
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from app.models import UserProfile, SwipeAction

@receiver(post_save, sender=SwipeAction)
def update_user_profile_num_swipes(sender, instance, created=False, **kwargs):
    swipe_instance = instance
    if created:
        if not swipe_instance.is_valid:
            if swipe_instance.is_vote:
                swipe_instance.on_user.num_right_swipes += 1
                swipe_instance.on_user.num_votes += 1
            else:
                if swipe_instance.is_right:
                    swipe_instance.on_user.num_right_swipes += 1
                else:
                    swipe_instance.on_user.num_left_swipes += 1
            swipe_instance.on_user.save()
            swipe_instance.is_valid = True
            swipe_instance.save()