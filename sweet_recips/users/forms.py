from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    email = forms.EmailField(label="Votre email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput)
    
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        
        if confirm_password != self.cleaned_data['password']:
            raise forms.ValidationError('Les mots de passes diffèrent !')
        
        return confirm_password
    
    def clean_email(self):
        email = self.cleaned_data['email']
        
        try:
            User.objects.get(email=email)
        except:
            forms.ValidationError("Cet email existe déjà, vous connectez")
        
        return email
           
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
             