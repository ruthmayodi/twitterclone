"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views as authviews
from twitteruser import views as userviews
from tweet import views as tweetviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userviews.index_view, name='home'),
    path('addtweet/', tweetviews.addtweet_view),
    path('notifications/<str:user_username>/', userviews.notification_view),
    path('tweet_detail/<int:tweet_id>/', userviews.tweet_view),
    path('login/', authviews.login_view),
    path('signup/', authviews.signup_view),
    path('logout/', authviews.logout_view),
    path('<str:user_username>/', userviews.profile_view),
    path('<str:user_username>/follow/', userviews.follow_view),
    path('<str:user_username>/unfollow/', userviews.unfollow_view),
]
