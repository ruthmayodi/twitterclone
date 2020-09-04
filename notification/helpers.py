from .models import Notification



def count_notifications(user_info):
    return Notification.objects.filter(notification_user=user_info).count()

