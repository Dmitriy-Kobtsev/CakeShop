# Generated by Django 5.1 on 2024-09-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
    ]