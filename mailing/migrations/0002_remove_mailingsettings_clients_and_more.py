# Generated by Django 4.2.4 on 2023-10-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingsettings',
            name='clients',
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='client',
            field=models.ManyToManyField(to='mailing.client', verbose_name='Client'),
        ),
    ]
