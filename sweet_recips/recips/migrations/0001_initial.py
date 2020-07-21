# Generated by Django 2.2.12 on 2020-07-20 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('photo', models.ImageField(null=True, upload_to='images_category')),
            ],
            options={
                'verbose_name': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indication', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name="Nom de l'ingredien")),
                ('photo', models.ImageField(null=True, upload_to='icon_ingredients/')),
            ],
            options={
                'verbose_name': 'Ingredient',
            },
        ),
        migrations.CreateModel(
            name='Recip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nom de la recette')),
                ('preparation', models.TextField(verbose_name='Description de la recette')),
                ('photo', models.ImageField(null=True, upload_to='images_recipes')),
                ('persons', models.IntegerField(null=True, verbose_name='Nombre de personne')),
                ('date', models.DateField(auto_now=True, verbose_name="Date d'ajout")),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recips.Category', verbose_name='Categorie')),
                ('ingredients', models.ManyToManyField(related_name='_recip_ingredients_+', through='recips.Composition', to='recips.Ingredient')),
            ],
            options={
                'verbose_name': 'Recette',
            },
        ),
        migrations.AddField(
            model_name='composition',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recips.Ingredient'),
        ),
        migrations.AddField(
            model_name='composition',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recips.Recip'),
        ),
    ]
