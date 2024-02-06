from django.db import models

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
