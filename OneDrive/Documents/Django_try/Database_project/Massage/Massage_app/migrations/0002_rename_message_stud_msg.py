# Generated by Django 5.1.3 on 2024-11-07 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Massage_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='message',
            new_name='msg',
        ),
    ]
