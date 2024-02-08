from django.contrib import admin
from django.contrib.admin import AdminSite
from django.views import View
from .models import Article, Categorie, Utilisateur, Contenu, Contact, Test
from django.shortcuts import render

# Register your models here.