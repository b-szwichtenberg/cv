# Generated by Django 4.0.5 on 2022-06-27 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0004_delete_gra'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Adres',
        ),
        migrations.DeleteModel(
            name='Gatunek',
        ),
        migrations.DeleteModel(
            name='Gra_gatunek',
        ),
        migrations.DeleteModel(
            name='Gra_polka',
        ),
        migrations.DeleteModel(
            name='Polka',
        ),
        migrations.DeleteModel(
            name='Producent',
        ),
        migrations.DeleteModel(
            name='Wydawca',
        ),
    ]
