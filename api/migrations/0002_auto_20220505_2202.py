# Generated by Django 3.0.8 on 2022-05-05 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liking',
            old_name='user',
            new_name='profile',
        ),
    ]
