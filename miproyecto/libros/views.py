#encoding:utf-8
from django.views.generic import TemplateView

from rest_framework import viewsets

from .models import Libro
from .serializers import LibroSerializer


class HomeTemplateView(TemplateView):
    """
    """

    template_name = 'home.html'


class LibroViewSet(viewsets.ModelViewSet):
    """
    
    """

    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
