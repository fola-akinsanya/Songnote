# Generated by Django 3.1.1 on 2020-09-30 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listener', '0012_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listenerfeedback',
            name='audio_file',
        ),
    ]
