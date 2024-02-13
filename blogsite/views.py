from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

import csv
import json


from .models import Article, Utilisateur, Contact, Categorie, StatUser
from .forms import MailForm, ContactForm


def index(request):
    latest_article = Article.objects.order_by("-pub_date")[1:4]
    last_article = Article.objects.order_by("-pub_date")[0:1]
    if len(last_article) != 0 :
        categories_last_article = last_article[0].categories.all()
    else:
        categories_last_article = "None"

    featured_article = Article.objects.filter(featured = 1).values()
    popular_article = Article.objects.order_by("-popular")[:6]
    categoriesID = list(Article.objects.values_list("categories"))
    categories = []

    for i in range(len(categoriesID)):
        a = list(Categorie.objects.raw("SELECT id,title FROM blogsite_categorie WHERE id ="+str(categoriesID[i][0])))
        categories.append(a)


    successForm = request.GET.get('successForm',False)


    if request.method=="POST":
        form = MailForm(request.POST)
        if form.is_valid():
            email = request.POST.get("mail")
            user = Utilisateur(mail=email)
            user.save()

            return redirect("./?successForm=True")

    else : 
        form = MailForm()

    context = {"latest_article" : latest_article, "featured_article": featured_article, "popular_article": popular_article, "last_article":last_article, "categories_last_article":categories_last_article,"form":form, "successForm":successForm, "categories":categories}


    return render(request, "blog/index.html", context)

def detail(request, slug):
    successForm = request.GET.get('successForm',False)
    successLike = request.GET.get('successLike', False)

    popular_article = Article.objects.order_by("-popular")[:3]


    form = MailForm(request.POST)
    if form.is_valid():
        email = request.POST.get("mail")
        user = Utilisateur(mail=email)
        user.save()

        return redirect("./detail/?successForm=True")

    else : 
         form = MailForm()
    
    article = get_object_or_404(Article, slug=slug)

    if article:
        article.views += 1
        article.save()

    if 'like' in request.POST:
        if request.session.get("has_liked" + slug, False):
            article.views -= 2
            return redirect("./?successLike=already")
        article.popular += 1
        article.views -= 2
        article.save()
        request.session["has_liked" + slug] = True
        request.session["has_disliked" + slug] = False

        return redirect("./?successLike=True")
    
    if 'dislike' in request.POST:
        if request.session.get("has_disliked" + slug, False):
            article.views -= 2
            return redirect("./?successLike=already")
        if(article.popular > 0):
            article.popular -= 1
        article.views -= 2
        article.save()
        request.session["has_liked" + slug] = False
        request.session["has_disliked" + slug] = True

        return redirect("./?successLike=True")

    context = {"article": article, "form":form, "successForm":successForm, "successLike":successLike, "popular_article": popular_article, "has_liked": request.session.get("has_liked" + slug), "has_disliked": request.session.get("has_disliked" + slug)}
    return render(request, "blog/detail.html", context)

def article(request):
    successForm = request.GET.get('successForm',False)
    if request.method == 'GET' and request.GET.get('search') != None:
        latest_article = Article.objects.filter(title__icontains=request.GET.get('search'))
    else : 
        latest_article = Article.objects.order_by("-pub_date")

    L = []
    for article in latest_article:
        art = []
        for cat in article.categories.all():
            art.append(cat)
        L.append(art)
        
            

    if request.method=="POST":
        form = MailForm(request.POST)
        if form.is_valid():
            email = request.POST.get("mail")
            user = Utilisateur(mail=email)
            user.save()

            return redirect("./?successForm=True")

    else : 
        form = MailForm()
    
    context = {"articles":latest_article, "form":form, "successForm":successForm, "liste":L}

    return render(request, "blog/article.html", context)

def contact(request):
    success=request.GET.get('success',False)
    successForm = request.GET.get('successForm',False)
    if request.method=="POST":
        formContact = ContactForm(request.POST)
        if formContact.is_valid():

            nom = request.POST.get("nom")
            prenom = request.POST.get("prenom")
            tel = request.POST.get("tel")
            sujet = request.POST.get("sujet")
            message = request.POST.get("message")

            contact = Contact(nom=nom, prenom=prenom, tel= tel, sujet=sujet, message=message)
            contact.save()
            return redirect("./?success=True")


    else : 
        formContact = ContactForm()
    
    if request.method=="POST":
        form = MailForm(request.POST)
        if form.is_valid():
            email = request.POST.get("mail")
            user = Utilisateur(mail=email)
            user.save()

            return redirect("./?successForm=True")

    else : 
        form = MailForm()


    context={"formContact":formContact, "form":form, "success":success, "successForm":successForm}

    return render(request, "blog/contact.html", context)

def about(request):
    successForm = request.GET.get('successForm',False)

    if request.method=="POST":
        form = MailForm(request.POST)
        if form.is_valid():
            email = request.POST.get("mail")
            user = Utilisateur(mail=email)
            user.save()

            return redirect("./?successForm=True")

    else : 
        form = MailForm()

    context={"form":form, "successForm":successForm}

    return render(request,"blog/about.html", context)

def Erreur404(request, exception):
    return render(request, '404.html', status=404)

def Erreur400(request, exception):
    return render(request, '400.html', status=400)

def Erreur500(request):
    return render(request, '500.html', status=500)

def stat(request):
    successForm = request.GET.get('successForm',False)

    fichier_naissance = open(str(settings.BASE_DIR) + "/blogsite/static/blog/naissance_data.csv", encoding="utf-8")
    csvreader_naissance = csv.reader(fichier_naissance)
    print(csvreader_naissance)
    y_naissance= []
    x_naissance = []
    rows_naissance = []

    for row in csvreader_naissance:
        rows_naissance.append(row)
    for r in rows_naissance:
        x_naissance.append(r[0])
        y_naissance.append(r[1])
        

    fichier_naissance.close()
    del(x_naissance[0])
    del(y_naissance[0])

    if request.method=="POST":
        form = MailForm(request.POST)
        if form.is_valid():
            email = request.POST.get("mail")
            user = Utilisateur(mail=email)
            user.save()

            return redirect("./?successForm=True")

    else : 
        form = MailForm()
    
    fichier = open(str(settings.BASE_DIR) + "/blogsite/static/blog/data.csv", encoding="utf-8")
    csvreader = csv.reader(fichier)
    d= []
    rows = []


    for row in csvreader:
        rows.append(row)
    for r in rows:
            d.append([r[3],r[8]])


    fichier.close()
    del(d[0])
    valeur_debut = request.POST.get("valeur_debut",0)
    valeur_fin = request.POST.get("valeur_fin",0)
    int_debut = request.POST.get("int_debut",1)
    int_fin = request.POST.get("int_fin",1)

    if (valeur_debut==0 and valeur_fin==0 and request.session.get("stat", False)):
        info = StatUser.objects.get(id = request.session["statid"])
        valeur_debut= info.date_debut
        valeur_fin = info.date_fin
        int_debut = info.int_debut
        int_fin = info.int_fin

    if request.session.get("stat", False):
        info = StatUser.objects.get(id = request.session["statid"])
        info.date_debut = valeur_debut
        info.date_fin = valeur_fin
        info.int_fin = int_fin
        info.int_debut = int_debut
        info.save()
    else:
        info = StatUser(date_debut=valeur_debut, date_fin = valeur_fin, int_debut = int_debut, int_fin = int_fin)
        info.save()
        request.session["statid"] = list(StatUser.objects.values('id'))[-1]["id"]
        request.session["stat"] = True

    context={"d1":d[:25], "d2":d[25:50],"d3":d[50:75],"d4":d[75:], "form":form, "successForm":successForm, "x_naissance":json.dumps(x_naissance), "y_naissance":json.dumps(y_naissance), "int_debut":int_debut, "int_fin":int_fin, "date_debut":valeur_debut, "date_fin":valeur_fin}
      
    return render(request, "blog/stat.html",context)

def com(request):
    fichier = open(str(settings.BASE_DIR) + "/blogsite/static/blog/data.csv", encoding="utf-8")
    csvreader = csv.reader(fichier)
    d= []
    rows = []

    for row in csvreader:
        rows.append(row)
    for r in rows:
            d.append([r[3],r[6]])

    fichier.close()
    del(d[0])

    context={"d1":d[:25], "d2":d[25:50],"d3":d[50:75],"d4":d[75:]}


    return render(request,"blog/tab-stat/com.html",context)

def pop(request):
    fichier = open(str(settings.BASE_DIR) + "/blogsite/static/blog/data.csv", encoding="utf-8")
    csvreader = csv.reader(fichier)
    d= []
    rows = []

    for row in csvreader:
        rows.append(row)
    for r in rows:
            d.append([r[3],r[8]])
    fichier.close()
    del(d[0])

    context={"d1":d[:25], "d2":d[25:50],"d3":d[50:75],"d4":d[75:]}


    return render(request,"blog/tab-stat/pop.html",context)