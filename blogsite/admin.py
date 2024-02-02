from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Article, Categorie, Utilisateur, Contenu, Contact, Test

admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Contenu)
admin.site.register(Categorie)
admin.site.register(Test)

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "pub_date", "mod_date"]
    ordering = ["-mod_date"]
    list_filter = ["mod_date"]
    search_fields = ["title"]


admin.site.register(Article, ArticleAdmin)

AdminSite.site_title="Test Django"
AdminSite.site_header="Test Django"