from django.views import generic
from app.models import UserProfile, Event
from django.http import HttpResponse, HttpResponseNotFound, Http404


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    model = UserProfile
    context_object_name = 'participants'

    def get_event(self):
        active_events = Event.objects.filter(is_active=True)
        if active_events.exists():
            return active_events.first()
        else:
            raise Http404

    def get_queryset(self, **kwargs):
        participants = self.get_event().participants.all()
        return participants

