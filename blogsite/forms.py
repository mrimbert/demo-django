from django import forms
from .models import Utilisateur, Contact, Article
from django.forms import EmailInput, ModelForm, TextInput, Textarea

class MailForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['mail']
        widgets = {
            'mail' : EmailInput(attrs={
                'class': "text-black w-96 rounded-lg",
                'placeholder':"Entrez votre e-mail"
            })
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'tel', 'sujet', 'message']
        widgets = {
            'nom' : TextInput(attrs = {
                'style':"max-width:500px;",
                'placeholder':"Nom",
            }),
            'prenom' : TextInput(attrs = {
                'style':"max-width:500px;",
                'placeholder':"Prénom",
            }),
            'tel' : TextInput(attrs = {
                'style':"max-width:300px;",
                'pattern':"[0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2}",
                'placeholder':"Tél (ex : 01-02-03-04-05)",
            }),
            'sujet' : TextInput(attrs = {
                'style':"max-width:300px;",
                'placeholder':"Sujet du message",
            }),
            'message' : Textarea(attrs = {
                'style':"max-width:500px;",
                'placeholder':"Message",
            })


        }
