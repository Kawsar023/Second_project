# Generated by Django 4.2.4 on 2023-09-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0010_alter_speaker_speaker_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='speaker_pic',
            field=models.ImageField(blank=True, null=True, upload_to='speaker_pic/'),
        ),
    ]