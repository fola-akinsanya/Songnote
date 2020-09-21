# Generated by Django 3.1.1 on 2020-09-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListenerQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_range', models.CharField(choices=[('16-19', '16-19'), ('20-24', '20-24'), ('25-34', '25-34'), ('35-44', '35-44'), ('45-54', '45-54'), ('55-64', '55-64'), ('65+', '65+')], max_length=40)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=12)),
                ('ethnic_group', models.CharField(choices=[('white-uk', 'White - English/Welsh/Scottish/Northern Irish'), ('white-irish', 'White - Irish'), ('white-gypsy', 'White - Gypsy or Irish Traveller'), ('white-other', 'White - Other'), ('mixed-white/carib', 'Mixed - White and Black Caribbean'), ('mixed-white/african', 'Mixed - White and Black African'), ('mixed-white/asian', 'Mixed - White and Asian'), ('mixed-other', ' Mixed - Other'), ('asian-indian', 'Asian - Indian'), ('asian-pakistani', 'Asian - Pakistani'), ('asian-bangladeshi', 'Asian - Bangladeshi'), ('asian-other', 'Asian - Other'), ('black-african', 'Black - African'), ('black-carib', 'Black - Caribbean'), ('black-other', 'Black - Other'), ('other-arab', 'Other - Arab'), ('other-other', 'Other - Any other ethnic group')], max_length=100)),
                ('favourite_genre', models.CharField(choices=[('rap', 'Rap'), ('rnb', 'RnB'), ('drill', 'Drill'), ('hip hop', 'Hip Hop'), ('grime', 'Grime'), ('afro swing', 'Afro Swing'), ('reggae', 'Reggae'), ('pop', 'Pop'), ('dubstep', 'Dubstep'), ('jazz', 'Jazz'), ('drum and bass', 'Drum and Bass'), ('rock', 'Rock'), ('heavy metal', 'Heavy Metal')], max_length=100)),
                ('artists_you_listen_to', models.TextField()),
                ('favourite_hangout_spots', models.TextField()),
            ],
        ),
    ]