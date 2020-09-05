from .models import Tweet
import re
from twitteruser.models import TwitterUser
from notification.models import Notification

def get_tweets(user_info):
    user_list = [user_info.id]
    for item in user_info.followed.all():
        user_list.append(item.id)
    tweets = Tweet.objects.filter(
        user__id__in=user_list
    ).order_by('-post_on')
    return tweets

    
def user_tweets(user_info):
    return Tweet.objects.filter(user__id=user_info.id).count()


def get_user_tweets(user_info):
    return Tweet.objects.filter(user__id=user_info.id).order_by('-post_on')


def parse_tweet(tweets):
    pattern = re.compile(r'(@)(\w+)(\s|$)')
    match_found = pattern.search(tweets.content)
    if match_found:
        username = match_found.group(2)
        user = TwitterUser.objects.get(username=username)
        if user:
            Notification.objects.create(
                notification_tweet=tweets,
                notification_user=user

            )
            return True
    return False


def get_tweet(tweet_id):
    return Tweet.objects.filter(id=tweet_id)