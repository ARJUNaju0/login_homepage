# Generated by Django 5.1.4 on 2025-04-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0002_remove_login_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='username',
        ),
    ]
