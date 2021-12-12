from django.urls import path
from .views import TrackView,TopTrackView

urlpatterns = [
    path('tracks/', TrackView.as_view(), name = 'tracks_list'),
    path('tracks/<int:id>', TrackView.as_view(), name = 'tracks_process'),
    path('tracks/top/<int:top>', TopTrackView.as_view(), name = 'tracks_process')

]