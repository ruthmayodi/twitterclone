from .models import Notification



def count_notifications(user_info):
    return Notification.objects.filter(notification_user=user_info).count()


def get_notifications(user_info):
    notify = []
    notifications = Notification.objects.filter(notification_user=user_info)
    for n in notifications:
        notify.append(n.notification_tweet.content)
    Notification.objects.filter(notification_user=user_info).delete()
    return notify
    

