# Generated by Django 4.0.5 on 2022-06-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_alter_adres_kod_alter_adres_miasto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producent',
            name='adres',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='wydawca',
            name='adres',
            field=models.CharField(max_length=100),
        ),
    ]