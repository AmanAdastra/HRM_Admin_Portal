# Generated by Django 3.1.7 on 2021-07-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_notifications_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]