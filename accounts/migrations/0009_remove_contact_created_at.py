# Generated by Django 5.1.3 on 2024-11-13 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_contact_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
    ]
