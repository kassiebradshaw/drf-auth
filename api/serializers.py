from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'artist', 'genre', 'listener', 'created_at', 'updated_at')
        model = Song