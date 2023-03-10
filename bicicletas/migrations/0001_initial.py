# Generated by Django 4.1.4 on 2022-12-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=150, verbose_name='Propietario')),
                ('marca', models.CharField(max_length=150, verbose_name='Marca')),
                ('neomaticos', models.CharField(max_length=150, verbose_name='neomaticos')),
                ('llantas', models.CharField(max_length=150, verbose_name='llantas')),
                ('cadena', models.CharField(max_length=150, verbose_name='cadena')),
                ('plato', models.CharField(max_length=150, verbose_name='plato')),
                ('cassette', models.CharField(max_length=150, verbose_name='cassette')),
                ('sistemafrenos', models.CharField(max_length=150, verbose_name='Sistema de frenos')),
                ('guayascambio', models.CharField(max_length=150, verbose_name='Guayas de Cambio')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
            options={
                'verbose_name': 'Estado bicicleta',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llantas', models.CharField(max_length=150, verbose_name='llantas')),
                ('neomaticos', models.CharField(max_length=150, verbose_name='neomaticos')),
                ('cadenas', models.CharField(max_length=150, verbose_name='cadenas')),
                ('platos', models.CharField(max_length=150, verbose_name='Platos')),
                ('cassettes', models.CharField(max_length=150, verbose_name='Cassettes')),
                ('guayascambio', models.CharField(max_length=150, verbose_name='Guayas de Cambio')),
                ('guayasfrenos', models.CharField(max_length=150, verbose_name='Guayas de frenos')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
        ),
    ]
