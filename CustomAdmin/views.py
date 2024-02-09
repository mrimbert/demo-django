from django.shortcuts import render

import json

from django.template.response import TemplateResponse

from blogsite.models import Article, Categorie, StatUser

 
 
def custom_app_view(request):
    article = list(Article.objects.values_list('title'))
    like = list(Article.objects.values_list('popular'))
    views = list(Article.objects.values_list('views'))
    date_debut = StatUser.objects.values_list("date_debut")
    date_debut_L = []
    date_fin = StatUser.objects.values_list("date_fin")
    date_fin_L = []

    for date in date_debut :
        a = StatUser.objects.filter(date_debut = ''.join(date)).count()
        date_debut_L.append(a)
    
    for date in date_fin:
        a = StatUser.objects.filter(date_fin = ''.join(date)).count()
        date_fin_L.append(a)
    
    date_debut = list(date_debut)
    date_fin = list(date_fin)

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
               'index_title': 'Informations administrateurs', 'article':json.dumps(article), 'like':json.dumps(like), 'views':json.dumps(views), 'views_per_like':json.dumps(views_per_like), "date_debut":json.dumps(date_debut),"date_fin":json.dumps(date_fin),"date_fin_L":json.dumps(date_fin_L),"date_debut_L":json.dumps(date_debut_L),"totalViews":totalViews, "totalLikes":totalLikes, "totalArticle":totalArticle, "totalCategorie":totalCategorie}
    return TemplateResponse(request, 'admin/custom_app_view.html', context)
