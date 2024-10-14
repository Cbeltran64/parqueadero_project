# Generated by Django 3.2.25 on 2024-10-13 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
        ),
    ]
