# Generated by Django 3.2.8 on 2022-01-23 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_live', models.BooleanField()),
                ('is_recording', models.BooleanField()),
                ('is_paid', models.BooleanField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='schedules.schedule')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='students.student')),
            ],
        ),
    ]
