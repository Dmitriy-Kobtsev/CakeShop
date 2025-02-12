# Generated by Django 5.1 on 2025-02-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0002_alter_products_category_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_filter',
            field=models.CharField(choices=[('mini_cake', 'mini_cake'), ('cake', 'cake'), ('frost', 'frost')], default='cake', max_length=20),
        ),
    ]
