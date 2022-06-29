# Generated by Django 4.0.5 on 2022-06-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=50, unique=True)),
                ('producent', models.CharField(max_length=50)),
                ('wydawca', models.CharField(max_length=50)),
                ('ocena', models.PositiveSmallIntegerField(default=0)),
                ('premiera', models.DateField(blank=True, null=True)),
                ('opis', models.TextField(default='')),
            ],
        ),
    ]
