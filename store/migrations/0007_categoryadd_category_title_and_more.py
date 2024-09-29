# Generated by Django 4.2.16 on 2024-09-29 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_job_details_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryadd',
            name='category_title',
            field=models.CharField(default='Consulting', max_length=500),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categoryadd'),
        ),
    ]
