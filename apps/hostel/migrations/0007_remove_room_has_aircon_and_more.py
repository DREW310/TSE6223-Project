# Generated by Django 4.2.7 on 2025-05-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_hostelapplication_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='has_aircon',
        ),
        migrations.RemoveField(
            model_name='room',
            name='has_attached_bathroom',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('single', 'Single Room'), ('double', 'Double Room')], max_length=10),
        ),
    ]
