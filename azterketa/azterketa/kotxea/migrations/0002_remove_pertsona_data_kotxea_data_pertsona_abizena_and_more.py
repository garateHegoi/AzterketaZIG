# Generated by Django 4.1.1 on 2022-10-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotxea', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pertsona',
            name='data',
        ),
        migrations.AddField(
            model_name='kotxea',
            name='data',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pertsona',
            name='abizena',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pertsona',
            name='izena',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
