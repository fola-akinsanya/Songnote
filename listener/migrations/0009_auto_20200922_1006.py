# Generated by Django 3.1.1 on 2020-09-22 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listener', '0008_auto_20200921_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listenerfeedback',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]