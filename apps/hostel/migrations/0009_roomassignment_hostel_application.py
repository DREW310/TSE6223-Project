# Generated by Django 4.2.7 on 2025-05-23 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0008_remove_room_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomassignment',
            name='hostel_application',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_assignment', to='hostel.hostelapplication'),
        ),
    ]
