# Generated by Django 4.2.4 on 2023-09-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0008_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='about_title',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speaker_pic',
            field=models.ImageField(blank=True, null=True, upload_to='speaker/'),
        ),
    ]
