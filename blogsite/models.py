from django.db import models

class Contenu(models.Model):
    contentTitle = models.CharField(max_length=200)
    paragraphe_1 = models.TextField()
    paragraphe_2 = models.TextField()
    paragraphe_3 = models.TextField()
    citation = models.TextField()
    citation_auteur = models.CharField(max_length=200)

    def __str__(self): 
        return self.contentTitle



class GeneralInformation(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    content = models.OneToOneField(
        Contenu,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    contexte = models.CharField(max_length=2000)

    class Meta:
        abstract = True

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title
    
class Article(GeneralInformation):
    mod_date = models.DateTimeField("date modified")
    categories = models.ManyToManyField(Categorie)
    featured = models.BooleanField()
    popular = models.IntegerField()
    image = models.CharField(max_length=300)
    image_illus = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Page(GeneralInformation):
    def __str__(self):
        return self.title
    
class Utilisateur(models.Model):
    mail = models.TextField(max_length=100)
    def __str__(self):
        return self.mail
    
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    sujet = models.CharField(max_length=1000)
    message = models.TextField()
    def __str__(self):
        return self.sujet
    
class Test(models.Model):
    upload = models.FileField(upload_to="blogsite/static/blog/images ")
