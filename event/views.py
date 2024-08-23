from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Events
from .serializers import EventSerializer
from rest_framework.exceptions import NotFound

class EventCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        # Retrieve all events from the database
        events = Events.objects.all()
        # Serialize the event data
        serializer = EventSerializer(events, many=True)
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        event_id = kwargs.get('id')       
        if event_id:
            # Retrieve a specific event by ID
            try:
                event = Events.objects.get(id=event_id)
            except Events.DoesNotExist:
                raise NotFound("Event not found.")
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Retrieve all events
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        event_id = kwargs.get('id')
        try:
            event = Events.objects.get(id=event_id)
        except Events.DoesNotExist:
            raise NotFound("Event not found.")
        
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        event_id = kwargs.get('id')
        try:
            event = Events.objects.get(id=event_id)
        except Events.DoesNotExist:
            raise NotFound("Event not found.")
        
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        event_id = kwargs.get('id')
        try:
            event = Events.objects.get(id=event_id)
        except Events.DoesNotExist:
            raise NotFound("Event not found.")
        
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
