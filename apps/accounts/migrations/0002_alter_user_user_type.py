# Generated by Django 4.2.7 on 2025-05-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin')], default='student', help_text='Type of user account', max_length=10),
        ),
    ]
