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
    slug = models.SlugField(default="",null=False)

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
    image = models.ImageField(upload_to="images/")
    image_illus = models.ImageField(upload_to="images/")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Page(GeneralInformation):
    def __str__(self):
        return self.title