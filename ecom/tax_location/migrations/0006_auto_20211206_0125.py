# Generated by Django 3.2.8 on 2021-12-05 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tax_location', '0005_auto_20211130_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxrates',
            name='zone',
        ),
        migrations.AddField(
            model_name='taxrates',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxrates',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]