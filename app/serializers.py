from rest_framework import serializers

from app.models import UserProfile, SwipeAction, Event

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'category', 
            'first_name',
            'last_name',
            'gender',
            'age',
            'num_right_swipes',
            'num_left_swipes',
            'num_views',
            'picture',
            )

class SwipeActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwipeAction
        fields = (
            'on_user', 
            'is_right',
            'event',
            'is_completed',
            )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'participants', 
            'name',
            'is_active',
            )
