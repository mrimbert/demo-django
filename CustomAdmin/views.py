from django.shortcuts import render

import json

from django.template.response import TemplateResponse

from blogsite.models import Article

 
 
def custom_app_view(request):
    article = list(Article.objects.values_list('title'))
    like = list(Article.objects.values_list('popular'))
    context = {'title': 'Statistique d\'utilisation', 'site_title': 'Custom App View', 'site_header': 'Informations générales',
               'index_title': 'Informations administrateurs', 'text': 'Custom App Text', 'article':json.dumps(article), 'like':json.dumps(like)}
    return TemplateResponse(request, 'admin/custom_app_view.html', context)
