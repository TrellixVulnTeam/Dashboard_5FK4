# Generated by Django 3.2.8 on 2021-11-29 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_subcategories_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategories_2',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategories'),
        ),
    ]