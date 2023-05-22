# Generated by Django 4.1.3 on 2023-05-22 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_timeslot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='start_time',
        ),
        migrations.AddField(
            model_name='timetable',
            name='time_slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.timeslot'),
        ),
    ]