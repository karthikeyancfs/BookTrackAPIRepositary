from rest_framework import serializers
from .models import *

class LibrarySerializer(serializers.ModelSerializer):
    library_name= serializers.CharField(read_only=True)
    class Meta:
        model=library
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(read_only=True)
    class Meta:
        model=book
        fields = "__all__"

class LibraryUserSerializer(serializers.ModelSerializer):
    library_user = serializers.CharField(read_only=True)
    class Meta:
        model=library_user
        fields = "__all__"

class LibraryBookSerializer(serializers.ModelSerializer):
    # book_title = serializers.CharField(source='book.title', read_only=True)
    # library_name = serializers.CharField(source='library.library_name', read_only=True)
    book = BookSerializer()
    library = LibrarySerializer()
    class Meta:
        model=library_book
        # fields = ('id', 'book_title', 'library_name', 'library','book')
        fields = ('id', 'library','book')

class LibraryActivitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='library_user.name', read_only=True)
    library_book = LibraryBookSerializer()
    
    class Meta:
        model=library_activity
        fields = ('id', 'activity_type', 'checked_out_at', 'checked_in_at', 'library_book', 'library_user', 'name')

class LibraryActivityUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='library_user.name', read_only=True)
    # library_book = LibraryBookSerializer()
    
    class Meta:
        model=library_activity
        fields = ('id', 'activity_type', 'checked_out_at', 'library_book', 'name')

class ActivityByLibrarySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='library_user.name', read_only=True)
    # library_book = LibraryBookSerializer()
    
    class Meta:
        model=library_activity
        fields = ('id', 'activity_type', 'checked_out_at', 'library_book', 'name')

class CheckoutLibraryBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='library_user.name', read_only=True)
    class Meta:
        model=library_activity
        fields = ('id', 'activity_type', 'checked_out_at', 'library_book', 'name')

class CheckinLibraryBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='library_user.name', read_only=True)
    class Meta:
        model=library_activity
        fields = ('id', 'activity_type', 'checked_in_at', 'library_book', 'name')