# Generated by Django 4.2.16 on 2024-09-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_job_details_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='category',
            field=models.CharField(default='Consulting', max_length=100),
        ),
    ]
