# Generated by Django 5.0.7 on 2024-08-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popularpeople', '0011_partner_m_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='people',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Draft Article'), (True, 'Actual Article')], default=0, verbose_name='Status'),
        ),
    ]
