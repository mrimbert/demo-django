"""
URL configuration for testdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from CustomAdmin.admin import admin_site

handler404 = 'blogsite.views.Erreur404'
handler400 = 'blogsite.views.Erreur400'
handler500 = 'blogsite.views.Erreur500'

for model, _ in admin.site._registry.items():
    admin_site.register(model)

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include("blogsite.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

