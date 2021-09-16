from django.urls import path
from .views import SongList, SongDetails

urlpatterns = [
    path('', SongList.as_view(), name='song_list'),
    path('<int:pk>/', SongDetails.as_view(), name='song_details'),
]