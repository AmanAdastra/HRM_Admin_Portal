# Generated by Django 3.2.4 on 2021-06-16 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0005_alter_foodinventory_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product_types',
        ),
    ]