# Generated by Django 5.1.3 on 2024-11-07 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Massage_app', '0003_rename_msg_stud_massage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='massage',
            new_name='msg',
        ),
    ]
