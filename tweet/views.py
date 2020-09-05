from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import AddTweetForm
from .models import Tweet
from .helpers import parse_tweet

# Create your views here.

def addtweet_view(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = Tweet.objects.create(
                content=data.get('content'),
                user=request.user
            )
            parse_tweet(new_user)           
            return HttpResponseRedirect(reverse('home'))
    form= AddTweetForm()
    return render(request, 'generic_form.html', {'form':form})

