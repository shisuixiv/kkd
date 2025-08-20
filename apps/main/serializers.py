from rest_framework import serializers

from .models import Library, Book, Author

class LibrarySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'title', 'description', 'image']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", 'title', 'description', 'author']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", 'title', 'description', 'price', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", 'name','birth_year']

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", 'title', 'description', 'price', 'author']
