# Generated by Django 3.1.7 on 2021-09-07 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sauron_ecommerce', '0002_auto_20210905_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='titre',
            field=models.TextField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='contenu',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='note',
            field=models.IntegerField(default=0),
        ),
    ]
