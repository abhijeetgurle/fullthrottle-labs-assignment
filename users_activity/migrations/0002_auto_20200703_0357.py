# Generated by Django 3.0.8 on 2020-07-03 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='timezone1',
            new_name='timezone',
        ),
    ]
