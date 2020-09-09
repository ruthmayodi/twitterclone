from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import AddTweetForm
from .models import Tweet
from .helpers import parse_tweet
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AddTweetView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        form= AddTweetForm()
        return render(request, 'generic_form.html', {'form':form})
    
    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = Tweet.objects.create(
                content=data.get('content'),
                user=request.user
            )
            parse_tweet(new_user)           
            return HttpResponseRedirect(reverse('home'))

