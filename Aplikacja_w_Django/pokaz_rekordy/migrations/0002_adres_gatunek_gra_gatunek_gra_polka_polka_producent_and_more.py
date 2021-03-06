# Generated by Django 4.0.5 on 2022-06-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokaz_rekordy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panstwo', models.CharField(max_length=50)),
                ('miasto', models.CharField(max_length=50)),
                ('kod', models.CharField(max_length=12)),
                ('ulica', models.CharField(max_length=50)),
                ('budynek', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gra_gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gra', models.CharField(max_length=50)),
                ('gatunek', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gra_polka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gra', models.CharField(max_length=50)),
                ('polka', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Polka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('strona', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wydawca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('strona', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=100)),
            ],
        ),
    ]
