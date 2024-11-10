# Generated by Django 5.1 on 2024-10-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0002_products_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category_filter',
            field=models.CharField(choices=[('frost', 'frost'), ('mini_cake', 'mini_cake'), ('cake', 'cake')], default='cake', max_length=20),
        ),
    ]
