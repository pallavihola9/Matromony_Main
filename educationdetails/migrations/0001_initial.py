# Generated by Django 4.2.6 on 2023-10-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
                ('occupation_details', models.CharField(max_length=150)),
                ('annual_income', models.CharField(max_length=150)),
                ('employed_in', models.CharField(max_length=150)),
                ('working_location', models.CharField(max_length=150)),
                ('special_cases', models.CharField(max_length=150)),
            ],
        ),
    ]
