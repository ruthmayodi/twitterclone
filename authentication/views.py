from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from .forms import SignupForm, LoginForm
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    def get(self, request):
        form= SignupForm()
        return render(request, 'generic_form.html', {'form':form})


    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))



class LoginView(TemplateView):
    def get(self, request):
        form = LoginForm()
        return render(request, 'generic_form.html', {'form':form})

    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = authenticate(
                request, 
                username=data.get('username'),
                password=data.get('password')
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))







