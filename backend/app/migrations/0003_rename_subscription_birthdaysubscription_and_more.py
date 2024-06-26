# Generated by Django 4.2 on 2024-06-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0002_alter_user_birth_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='BirthdaySubscription',
        ),
        migrations.RenameField(
            model_name='birthdaysubscription',
            old_name='subscribed_to',
            new_name='subscribee',
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='app_user_set', related_query_name='user', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='app_user_set', related_query_name='user', to='auth.permission'),
        ),
        migrations.AlterUniqueTogether(
            name='birthdaysubscription',
            unique_together={('subscriber', 'subscribee')},
        ),
    ]
