# Generated by Django 3.0.8 on 2020-08-12 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CR-Fairmount', 'Fairmount Line'), ('CR-Fitchburg', 'Fitchburg Line'), ('CR-Worcester', 'Framingham/Worcester Line'), ('CR-Franklin', 'Franklin Line/Foxboro Pilot'), ('CR-Greenbush', 'Greenbush Line'), ('CR-Haverhill', 'Haverhill Line'), ('CR-Kingston', 'Kingston/Plymouth Line'), ('CR-Lowell', 'Lowell Line'), ('CR-Middleborough', 'Middleborough/Lakeville Line'), ('CR-Needham', 'Needham Line'), ('CR-Newburyport', 'Newburyport/Rockport Line'), ('CR-Providence', 'Providence/Stoughton Line'), ('CR-Foxboro', 'Foxboro Event Service')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_stop', models.CharField(max_length=50)),
                ('starting_time', models.TimeField()),
                ('ending_stop', models.CharField(max_length=50)),
                ('ending_time', models.TimeField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnTime.Line')),
            ],
        ),
    ]
