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
                'style': "max-width:300px;",
                'placeholder':"Entrez votre e-mail"
            })
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'tel', 'sujet', 'message']
        widgets = {
            'nom' : TextInput(attrs = {
                'class':"block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer",
                'style':"max-width:500px;",
                'placeholder':"Entrez votre nom",
            }),
            'prenom' : TextInput(attrs = {
                'class':"block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer",
                'style':"max-width:500px;",
                'placeholder':"Entrez votre prénom",
            }),
            'tel' : TextInput(attrs = {
                'class': "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer",
                'style':"max-width:300px;",
                'pattern':"[0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2}",
                'placeholder':"Entrez votre téléphone",
            }),
            'sujet' : TextInput(attrs = {
                'class':"block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer",
                'style':"max-width:300px;",
                'placeholder':"Saisir le sujet du message",
            }),
            'message' : Textarea(attrs = {
                'class':"block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-non focus:outline-none focus:ring-0 focus:border-blue-600 peer",
                'style':"max-width:500px;",
                'placeholder':"Saisissez-votre message",
            })


        }
