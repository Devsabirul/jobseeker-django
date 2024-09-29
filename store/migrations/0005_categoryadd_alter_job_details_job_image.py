# Generated by Django 4.2.16 on 2024-09-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_featuresjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Media/Category Image')),
            ],
        ),
        migrations.AlterField(
            model_name='job_details',
            name='job_image',
            field=models.ImageField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeDkSNW9wtNePKrUAr1M8nbZvLO5AF8t0TMg&s', upload_to='Media/jobImage'),
        ),
    ]
