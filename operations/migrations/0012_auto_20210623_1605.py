# Generated by Django 3.0.7 on 2021-06-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0011_foodinventory_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinventory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]