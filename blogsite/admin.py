from django.contrib import admin
from django.contrib.admin import AdminSite
from django.views import View
from .models import Article, Categorie, Utilisateur, Contenu, Contact, Test
from django.shortcuts import render

admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Contenu)
admin.site.register(Categorie)
admin.site.register(Test)

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "pub_date", "mod_date", "popular"]
    ordering = ["-mod_date"]
    list_filter = ["mod_date", "popular"]
    search_fields = ["title"]
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Article, ArticleAdmin)

AdminSite.site_title="Test Django"
AdminSite.site_header="Test Django"