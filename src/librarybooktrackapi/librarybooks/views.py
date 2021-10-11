from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class LibraryViewSet(viewsets.ModelViewSet):
    """ Library Details - GET, POST, UPDATE, PUT, DELETE """
    queryset = library.objects.all()
    serializer_class=LibrarySerializer

class BookViewSet(viewsets.ModelViewSet):
    """ Book Details - GET, POST, UPDATE, PUT, DELETE """
    queryset = book.objects.all()
    serializer_class=BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ User Details - GET, POST, UPDATE, PUT, DELETE """
    queryset = library_user.objects.all()
    serializer_class=LibraryUserSerializer

class LibraryBookViewSet(viewsets.ModelViewSet):
    """ Library Book Connection """
    queryset = library_book.objects.all()
    serializer_class=LibraryBookSerializer

class LibraryActivityViewSet(viewsets.ModelViewSet):
    """ Detailed Library activity list """
    queryset = library_activity.objects.all()
    serializer_class=LibraryActivitySerializer

class CheckoutLibraryBookViewSet(viewsets.ModelViewSet):
    " Check out books - GET, POST, UPDATE, PUT DELETE "
    queryset = library_activity.objects.all()
    serializer_class=CheckoutLibraryBookSerializer

class CheckinLibraryBookViewSet(viewsets.ModelViewSet):
    " Check in books - GET, POST, UPDATE, PUT DELETE "
    queryset = library_activity.objects.all()
    serializer_class=CheckinLibraryBookSerializer

class BookCheckoutByUserviewset(viewsets.ModelViewSet):
    ''' List the checkout books by user '''
    queryset = library_activity.objects.all()
    serializer_class=LibraryActivityUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activity_type', 'library_user']

class BookCheckoutFromLibraryviewset(viewsets.ModelViewSet):
    ''' List the checkout books by library '''
    queryset = library_activity.objects.all()
    serializer_class=ActivityByLibrarySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activity_type', 'library_book']