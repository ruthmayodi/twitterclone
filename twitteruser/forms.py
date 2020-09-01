from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TwitterUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = TwitterUser
        fields = ('username', 'email')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TwitterUser
        fields = ('username', 'email')
        
