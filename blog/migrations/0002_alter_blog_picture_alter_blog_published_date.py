# Generated by Django 4.2.1 on 2023-10-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.ImageField(upload_to='blog/', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=0, null=True, verbose_name='Published time'),
        ),
    ]
