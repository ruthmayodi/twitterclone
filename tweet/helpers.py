from .models import Tweet

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