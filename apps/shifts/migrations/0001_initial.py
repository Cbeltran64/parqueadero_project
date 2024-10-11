# Generated by Django 3.2.25 on 2024-10-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.DateTimeField(auto_now_add=True)),
                ('close_time', models.DateTimeField(blank=True, null=True)),
                ('total_income', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
