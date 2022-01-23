# Generated by Django 4.0.1 on 2022-01-23 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
