# Generated by Django 4.1.13 on 2024-02-12 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('tipoVehiculo', models.CharField(choices=[('Coche', 'Coche'), ('Ciclomotor', 'ciclomotor'), ('Motocicleta', 'Motocicleta')], max_length=100)),
                ('matricula', models.CharField(max_length=100, unique=True)),
                ('suspendido', models.BooleanField(default=False)),
                ('fecha_fabricacion', models.DateField()),
                ('fecha_baja', models.DateField()),
                ('fecha_matricula', models.DateField()),
                ('chasis', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marca')),
            ],
        ),
    ]
