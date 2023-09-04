from django.contrib import admin
from .models import Book, Book_instance, Author, Genre, Language

# Register your models here.

admin.site.register(Book)
admin.site.register(Book_instance)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)