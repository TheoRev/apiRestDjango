from .views import ListaVideo, DetailVideo
from django.urls import path

urlpatterns = [
    path('videos/', ListaVideo.as_view(), name='lista-video'),
    path('videos/<int:pk>', DetailVideo.as_view(), name='detail-video'),
]
