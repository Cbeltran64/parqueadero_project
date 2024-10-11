# Generated by Django 3.2.25 on 2024-10-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('users', '0002_auto_20241010_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='menu_permissions',
        ),
        migrations.AddField(
            model_name='customuser',
            name='menu_permissions',
            field=models.ManyToManyField(related_name='permitted_users', to='menu.MenuOption'),
        ),
    ]
