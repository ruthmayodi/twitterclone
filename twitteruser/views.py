from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.helpers import get_tweets, user_tweets, get_user_tweets
from notification.helpers import count_notifications


# Create your views here.
@login_required
def index_view(request):
    user_info=TwitterUser.objects.get(id=request.user.id)
    followed_count = user_info.followed.all().count()
    tweets = get_tweets(user_info)
    count_tweet = user_tweets(user_info)
    count_notify = count_notifications(user_info)
    
    return render(request, 'index.html', {
        'user_info': user_info,
        'followed_count': followed_count,
        'tweets': tweets,
        'tweet_count': count_tweet, 
        'notif_count': count_notify,
        'template_name': 'tweets.html'
    })

def profile_view(request, user_username):
    user_info=TwitterUser.objects.get(username=user_username)
    followed_count = user_info.followed.all().count()
    tweets = get_user_tweets(user_info)
    count_tweet = user_tweets(user_info)
    count_notify = count_notifications(user_info)
    
    return render(request, 'index.html', {
        'user_info': user_info,
        'followed_count': followed_count,
        'tweets': tweets,
        'tweet_count': count_tweet, 
        'notif_count': count_notify,
        'template_name': 'tweets.html'
    })

