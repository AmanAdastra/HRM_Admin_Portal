# Generated by Django 3.2.4 on 2021-06-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_auto_20210616_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinventory',
            name='type',
            field=models.CharField(choices=[('Snacks', 'Snacks'), ('Beverages', 'Beverages'), ('Others', 'Others')], default='Snacks', max_length=50),
        ),
    ]