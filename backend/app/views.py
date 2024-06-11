from datetime import datetime

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, RegisterForm
from .models import BirthdaySubscription, User


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'user_list.html', {'users': users})


@login_required
def subscribe(request, user_id):
    user_to_subscribe = get_object_or_404(User, id=user_id)
    BirthdaySubscription.objects.get_or_create(subscriber=request.user, subscribee=user_to_subscribe)
    return redirect('user_list')


@login_required
def subscriptions(request):
    subscriptions = BirthdaySubscription.objects.filter(subscriber=request.user)
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions})


@login_required
def unsubscribe(request, user_id):
    user_to_unsubscribe = get_object_or_404(User, id=user_id)
    subscription = BirthdaySubscription.objects.filter(subscriber=request.user, subscribee=user_to_unsubscribe)
    if subscription.exists():
        subscription.delete()
    return redirect('subscriptions')


@login_required
def unsubscribe_all(request):
    BirthdaySubscription.objects.filter(subscriber=request.user).delete()
    return redirect('subscriptions')


def send_birthday_notifications():
    today = datetime.today().date()
    subscriptions = BirthdaySubscription.objects.filter(subscribee__birth_date=today)
    for subscription in subscriptions:
        send_mail(
            'Birthday Reminder',
            f"Today is {subscription.subscribee.username}'s birthday!",
            settings.DEFAULT_FROM_EMAIL,
            [subscription.subscriber.email],
            fail_silently=False,
        )
