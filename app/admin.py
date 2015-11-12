from django.contrib import admin

from app.models.models import UserProfile, Event, SwipeAction

admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(SwipeAction)
