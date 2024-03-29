from django.urls import path

from . import views

app_name = "blogsite"
urlpatterns = [
        path("", views.index, name="index"),
        path("article/", views.article, name="article"),
        path("<slug:slug>/detail/", views.detail, name="detail"),
        path("contact/", views.contact, name="contact"),
        path("about/", views.about, name="about"),
        path("stat/", views.stat, name='stat'),
        path("com/", views.com, name="com"),
        path("pop/", views.pop, name="pop")
]