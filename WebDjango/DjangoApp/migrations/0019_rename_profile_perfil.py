# Generated by Django 3.2.14 on 2022-07-19 21:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoApp', '0018_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Perfil',
        ),
    ]
