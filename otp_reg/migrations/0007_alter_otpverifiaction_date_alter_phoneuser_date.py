# Generated by Django 4.2.6 on 2023-12-05 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_reg', '0006_alter_otpverifiaction_date_alter_phoneuser_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpverifiaction',
            name='date',
            field=models.CharField(default='2023-12-05', max_length=10),
        ),
        migrations.AlterField(
            model_name='phoneuser',
            name='date',
            field=models.CharField(default='2023-12-05', max_length=10),
        ),
    ]
