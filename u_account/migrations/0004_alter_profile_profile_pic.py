# Generated by Django 4.2.16 on 2024-09-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u_account', '0003_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='https://uxwing.com/wp-content/themes/uxwing/download/peoples-avatars/default-avatar-profile-picture-male-icon.png', upload_to='Media/profile image'),
        ),
    ]
