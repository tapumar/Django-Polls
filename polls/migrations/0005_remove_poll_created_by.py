# Generated by Django 2.1.4 on 2018-12-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181206_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='created_by',
        ),
    ]