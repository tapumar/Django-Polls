# Generated by Django 2.1.4 on 2018-12-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]