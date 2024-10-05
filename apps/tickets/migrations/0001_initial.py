# Generated by Django 3.2.25 on 2024-09-25 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_plate', models.CharField(max_length=10)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1)),
                ('generated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customuser')),
            ],
            options={
                'verbose_name': 'Tiquete',
                'verbose_name_plural': 'Tiquetes',
            },
        ),
    ]
