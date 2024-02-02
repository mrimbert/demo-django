from django.urls import path

from . import views

app_name = "blogsite"
urlpatterns = [
        path("", views.index, name="index"),
        path("/", views.index, name="index-button"),
        path("article/", views.article, name="article"),
        path("<int:article_id>/detail", views.detail, name="detail"),
        path("contact/", views.contact, name="contact"),
        path("about/", views.about, name="about"),
]