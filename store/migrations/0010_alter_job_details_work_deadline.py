# Generated by Django 4.2.16 on 2024-09-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='work_deadline',
            field=models.DateTimeField(),
        ),
    ]
