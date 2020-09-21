# Generated by Django 3.1.1 on 2020-09-21 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listener', '0003_auto_20200921_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='listenerfeedback',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
