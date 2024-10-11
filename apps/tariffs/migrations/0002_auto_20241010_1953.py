# Generated by Django 3.2.25 on 2024-10-11 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_convenio', models.CharField(max_length=100, unique=True)),
                ('porcentaje_descuento', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='fixed_price',
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='max_duration_fixed',
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='name',
        ),
        migrations.AddField(
            model_name='tariff',
            name='nombre_tarifa',
            field=models.CharField(default='Tarifa Genérica', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='vehicle_type',
            field=models.CharField(choices=[('car', 'Carro'), ('motorcycle', 'Moto'), ('bicycle', 'Bicicleta')], max_length=20),
        ),
        migrations.AddField(
            model_name='tariff',
            name='convenio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifas', to='tariffs.convenio'),
        ),
    ]
