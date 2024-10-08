# Generated by Django 4.2.2 on 2024-02-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='COST_PRICE',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROFIT_MARGIN',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='SEASON',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='SELLING_PRICE',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
