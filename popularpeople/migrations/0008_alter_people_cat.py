# Generated by Django 5.0.7 on 2024-08-10 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popularpeople', '0007_category_people_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='popularpeople.category'),
        ),
    ]
