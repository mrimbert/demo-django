from django.shortcuts import render

from django.template.response import TemplateResponse
 
 
def custom_app_view(request):
    context = {'title': 'Statistique d\'utilisation', 'site_title': 'Custom App View', 'site_header': 'Informations générales',
               'index_title': 'Informations administrateurs', 'text': 'Custom App Text'}
    return TemplateResponse(request, 'admin/custom_app_view.html', context)
