# Generated by Django 2.2.12 on 2020-07-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recip',
            name='ingredients_length',
            field=models.IntegerField(default=1, null=True),
        ),
    ]