from django.contrib import admin
from .models import Article, Categorie, Utilisateur, Contenu, Contact

admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Contenu)

# Register your models here.