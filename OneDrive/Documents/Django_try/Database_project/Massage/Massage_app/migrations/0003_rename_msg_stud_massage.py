# Generated by Django 5.1.3 on 2024-11-07 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Massage_app', '0002_rename_message_stud_msg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='msg',
            new_name='massage',
        ),
    ]
