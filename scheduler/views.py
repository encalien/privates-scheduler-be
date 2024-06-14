from rest_framework import generics

from scheduler.models import TimeSlot
from scheduler.serializers.timeslot_serializer import TimeslotSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the scheduler index.")

class TimeslotListCreateView(generics.ListCreateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeslotSerializer

class TimeslotRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeslotSerializer