from rest_framework import serializers
from .models import Events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'Title', 'Description', 'Event_Cost']