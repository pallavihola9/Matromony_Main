# Generated by Django 4.2.6 on 2024-01-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_auth_provider_user_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profileImage/'),
        ),
    ]
