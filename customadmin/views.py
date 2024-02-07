from django.shortcuts import render

from django.template.response import TemplateResponse
 
 
def chart_view(request):
    context = {'title': 'Custom App View', 'site_title': 'Custom App View', 'site_header': 'Custom App Header',
               'index_title': 'Custom App', 'text': 'Custom App Text'}
    return TemplateResponse(request, 'admin/chart.html', context)
