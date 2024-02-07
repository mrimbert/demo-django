from django.shortcuts import render

import json

from django.template.response import TemplateResponse

from blogsite.models import Article, Categorie

 
 
def custom_app_view(request):
    article = list(Article.objects.values_list('title'))
    like = list(Article.objects.values_list('popular'))
    views = list(Article.objects.values_list('views'))
    views_per_like = []
    totalViews =0
    totalLikes = 0
    totalArticle = 0
    totalCategorie = Categorie.objects.count()
    for i in range(len(like)):
        if views[i][0] != 0:
            views_per_like.append(like[i][0]/views[i][0])
        else:
            views_per_like.append(0)
        totalViews += views[i][0]
        totalLikes += like[i][0]
        totalArticle += 1
    context = {'title': 'Statistique d\'utilisation', 'site_title': 'Administration du site', 'site_header': 'Informations générales',
               'index_title': 'Informations administrateurs', 'article':json.dumps(article), 'like':json.dumps(like), 'views':json.dumps(views), 'views_per_like':json.dumps(views_per_like), "totalViews":totalViews, "totalLikes":totalLikes, "totalArticle":totalArticle, "totalCategorie":totalCategorie}
    return TemplateResponse(request, 'admin/custom_app_view.html', context)
