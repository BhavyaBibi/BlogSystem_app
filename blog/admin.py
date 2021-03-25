from django.contrib import admin
from .models import Post, Author, Categorie
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Categorie)