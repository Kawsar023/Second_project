# Generated by Django 4.2.4 on 2023-08-27 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0005_rename_speakers_designation_speakers_desi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speakers',
            name='desi',
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='pinterest',
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='twitter',
        ),
        migrations.DeleteModel(
            name='designations',
        ),
    ]