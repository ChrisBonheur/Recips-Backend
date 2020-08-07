from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

from .forms import UserForm, ConnexionForm

def create_user(request):
    form = UserForm(request.POST or None)
    email_exist = False
    username_exist = False
    
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        check_email = User.objects.filter(email=email)
        check_username = User.objects.filter(username=username)
        
        if not check_email and not check_username:
            new_user = User.objects.create_user(username, email, password)
            # user =  authenticate(email=email, password=password)
            # login(request, user)
            
            return redirect('recips:home')
        elif check_email:
            email_exist = True
        elif check_username:
            username_exist = True
        
    return render(request, 'users/create-user.html', locals())

# class Connexion(TemplateView):
#     template_name = 'users/connexion.html'
    
#     def get_context_data(self, **kwargs):
#         forms = ConnexionForm()
#         context = super(Connexion, self).get_context_data(**kwargs)
#         context['forms'] = forms
        
#         return context
    
def connexion(request):
    error = False
    
    if request.method == "POST":
        forms = ConnexionForm(request.POST)
        
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('recips:home')
            else:
                error = True
    else:
        forms = ConnexionForm()
                
    return render(request, 'users/connexion.html', locals())


def deconnexion(request):
    logout(request)
    
    return redirect('users:connexion')