from rest_framework import serializers
from .models import Libro


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Libro
        fields = ('id', 'titulo', 'autor',)