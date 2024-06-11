from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='app_user_set',
        blank=True,
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='app_user_set',
        blank=True,
        related_query_name='user',
    )


class BirthdaySubscription(models.Model):
    subscriber = models.ForeignKey(
        User,
        related_name='subscriptions',
        on_delete=models.CASCADE
    )
    subscribee = models.ForeignKey(
        User,
        related_name='subscribers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('subscriber', 'subscribee')

    def __str__(self):
        return f"{self.subscriber} subscribed to {self.subscribee}"
