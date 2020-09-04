from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from .forms import SignupForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
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
    form= SignupForm()
    return render(request, 'generic_form.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
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
    form = LoginForm()
    return render(request, 'generic_form.html', {'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))







