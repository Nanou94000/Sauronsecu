# Generated by Django 3.1.7 on 2021-09-05 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.TextField(help_text='nom du produit', max_length=100)),
                ('description', models.TextField(help_text='une description attractif du produit', max_length=200)),
                ('image', models.ImageField(default=0, upload_to=None)),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payer', models.BooleanField(default=False)),
                ('date_payer', models.DateTimeField()),
            ],
            options={
                'ordering': ['date_payer'],
            },
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField(max_length=200, null=True)),
            ],
            options={
                'ordering': ['total'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(help_text='nom du produit', max_length=100, unique=True)),
                ('description', models.TextField(help_text='une description attractif du produit', max_length=200)),
                ('prix', models.FloatField(help_text='le prix du produit en euro')),
                ('date_ajout', models.DateTimeField()),
                ('poids', models.FloatField(help_text='poids du produit en gramme', null=True)),
                ('resolution', models.TextField(choices=[('none', 'none'), ('1080', 'hd'), ('2160', 'hd+'), ('4320', '4k'), ('8640', '8k')])),
                ('image1', models.ImageField(default='null', null=True, upload_to=None)),
                ('image2', models.ImageField(default='null', null=True, upload_to=None)),
                ('image3', models.ImageField(default='null', null=True, upload_to=None)),
                ('image4', models.ImageField(default='null', null=True, upload_to=None)),
                ('image5', models.ImageField(default='null', null=True, upload_to=None)),
                ('note', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['nom', 'date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField(help_text='Quantité de produit en stock')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.produit')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.TextField(help_text='nom du produit', max_length=100)),
                ('description', models.TextField(help_text='une description attractif du produit', max_length=200)),
                ('image', models.ImageField(default=0, upload_to=None)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.categorie')),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(default='', max_length=200)),
                ('code_postal', models.CharField(default='00000', help_text='Entrez votre code postal', max_length=6)),
                ('pays', models.CharField(default='France', max_length=50)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(default='null', null=True, upload_to='sauron_ecommerce/static/profileImage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProduitPanier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField()),
                ('quantite', models.IntegerField(default=0)),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sauron_ecommerce.panier')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sauron_ecommerce.produit')),
            ],
            options={
                'ordering': ['date_joined'],
            },
        ),
        migrations.AddField(
            model_name='produit',
            name='souscategorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.souscategorie'),
        ),
        migrations.AddField(
            model_name='panier',
            name='produitspanier',
            field=models.ManyToManyField(through='sauron_ecommerce.ProduitPanier', to='sauron_ecommerce.Produit'),
        ),
        migrations.AddField(
            model_name='panier',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.profile'),
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('etat', models.BooleanField(default=False, help_text='Paiement accepté ou pas')),
                ('commande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.commande')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.profile')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenu', models.TextField(max_length=500)),
                ('note', models.IntegerField(null=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.produit')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.profile')),
            ],
            options={
                'ordering': ['profile'],
            },
        ),
        migrations.AddField(
            model_name='commande',
            name='panier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.panier'),
        ),
        migrations.AddField(
            model_name='commande',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sauron_ecommerce.profile'),
        ),
    ]
