# Generated by Django 5.1 on 2024-10-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0004_alter_products_category_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_filter',
            field=models.CharField(choices=[('cake', 'cake'), ('frost', 'frost'), ('mini_cake', 'mini_cake')], default='cake', max_length=20),
        ),
    ]
