from rest_framework import serializers

from scheduler.models import TimeSlot

class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'