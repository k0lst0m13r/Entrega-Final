# Generated by Django 3.2.14 on 2022-07-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0028_alter_avatar_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(null=True, upload_to='avatar/'),
        ),
    ]
