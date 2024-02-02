from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext



from .models import Article, Utilisateur, Contact
from .forms import MailForm, ContactForm


def index(request):
    latest_article = Article.objects.order_by("-pub_date")[1:4]
    last_article = Article.objects.order_by("-pub_date")[0:1]
    categories_last_article = last_article[0].categories.all()

    featured_article = Article.objects.filter(featured = 1).values()
    popular_article = Article.objects.order_by("-popular")[:6]

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

    context = {"latest_article" : latest_article, "featured_article": featured_article[0], "popular_article": popular_article, "last_article":last_article[0], "categories_last_article":categories_last_article,"form":form, "successForm":successForm}


    return render(request, "blog/index.html", context)

def detail(request, article_id):
    successForm = request.GET.get('successForm',False)

    form = MailForm(request.POST)
    if form.is_valid():
        email = request.POST.get("mail")
        user = Utilisateur(mail=email)
        user.save()

        return redirect("./detail/?successForm=True")

    else : 
         form = MailForm()
    
    article = get_object_or_404(Article, pk=article_id)
    context = {"article": article, "form":form, "successForm":successForm}
    return render(request, "blog/detail.html", context)

def article(request):
    successForm = request.GET.get('successForm',False)
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