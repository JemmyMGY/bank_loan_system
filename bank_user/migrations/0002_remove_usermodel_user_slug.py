# Generated by Django 4.1.2 on 2023-01-04 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='user_slug',
        ),
    ]