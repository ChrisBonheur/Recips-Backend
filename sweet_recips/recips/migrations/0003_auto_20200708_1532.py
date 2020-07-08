# Generated by Django 2.2.12 on 2020-07-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recips', '0002_auto_20090817_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Categorie',
            },
        ),
        migrations.AlterField(
            model_name='recip',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nom de la recette'),
        ),
        migrations.AlterField(
            model_name='recip',
            name='photo',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='recip',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recips.Category', verbose_name='Categorie'),
        ),
    ]
