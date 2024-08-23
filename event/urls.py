from django.urls import path
from .views import EventCreateAPIView

urlpatterns = [
    path('create_events/', EventCreateAPIView.as_view(), name='event-create'),
    path('get_events/', EventCreateAPIView.as_view(), name='event-get'),
    path('get_event/<int:id>/', EventCreateAPIView.as_view(), name='event-filter'),
    path('get_event/<int:id>/', EventCreateAPIView.as_view(), name='event-filter'),
]