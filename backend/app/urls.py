from django.urls import path

from .views import (index, profile, register, subscribe, subscriptions,
                    unsubscribe, unsubscribe_all, user_list, user_login,
                    user_logout)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('users/', user_list, name='user_list'),
    path('subscribe/<int:user_id>/', subscribe, name='subscribe'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('unsubscribe/<int:user_id>/', unsubscribe, name='unsubscribe'),
    path('unsubscribe_all/', unsubscribe_all, name='unsubscribe_all'),
]
