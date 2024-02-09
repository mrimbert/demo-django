from django.contrib import admin
from django.urls import path
from .views import custom_app_view
from blogsite.models import Article, Categorie, Utilisateur, Contenu, Contact, Test, StatUser
from django.shortcuts import render
 
class CustomAppAdmin(admin.AdminSite):
    index_template = 'admin/custom_index.html'
    site_title = site_header = index_title = 'Site d\'administration'
 
    def get_urls(
        self,
    ):
        return [
            path(
                "custom-app/",
                self.admin_view(custom_app_view),
                name="custom_app_index",
            ),
        ] + super().get_urls()
 
 
admin_site = CustomAppAdmin()

admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Contenu)
admin.site.register(Categorie)

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "pub_date", "mod_date", "popular"]
    ordering = ["-mod_date"]
    list_filter = ["mod_date", "popular"]
    search_fields = ["title"]
    prepopulated_fields = {"slug":("title",)}

class StatUserAdmin(admin.ModelAdmin):
    list_display = ["date_debut","date_fin"]

admin_site.register(StatUser,StatUserAdmin)
admin_site.register(Article, ArticleAdmin)