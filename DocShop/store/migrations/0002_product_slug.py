# Generated by Django 4.1 on 2022-08-31 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
