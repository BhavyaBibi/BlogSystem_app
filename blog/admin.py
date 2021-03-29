from django.contrib import admin
from .models import Post, Author, Categorie, subscribe, Contact,Comment,SubComment
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Categorie)
admin.site.register(subscribe)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(SubComment)