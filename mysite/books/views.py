from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Action')
    serializer_class = BookSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Comedy')
    serializer_class = BookSerializer

class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Adventure')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Horror')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer


class DramaViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Drama')
    serializer_class = BookSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Thriller')
    serializer_class = BookSerializer

class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fiction')
    serializer_class = BookSerializer


class NonFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='NonFiction')
    serializer_class = BookSerializer

